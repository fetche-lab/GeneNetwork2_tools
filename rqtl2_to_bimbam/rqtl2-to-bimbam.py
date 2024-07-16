"""
Fred's snippets for the R/qtl2 to BIMBAM conversion script from Felix
"""
import sys
import argparse
import pandas as pd 

def rqtl2genotype_to_bimbam(genotype_file, alleles_file, encoding, output_file=None):
    """
    Processes the rqtl2 genotype file and converts it to BIMBAM format.
    Args:
        genotype_file (str): Path to the genotype file in CSV format.
        alleles_file (str): Path to the alleles file in CSV format.
        encoding (str): Encoding scheme for the genotype data (e.g., "AA=0,AB=1,BB=2").
        output_file (str, optional): Path to the output BIMBAM file in CSV format.

    """
    
    # Load the input files
    genotype_df = pd.read_csv(genotype_file)
    alleles_df = pd.read_csv(alleles_file)

    # Add columns from alleles_df to genotype_df
    genotype_df.insert(1, 'minor', alleles_df['minor'])
    genotype_df.insert(2, 'major', alleles_df['major'])

    # Parse the encoding scheme
    encoding_dict = {}
    for pair in encoding.split(','):
        allele, value = pair.split('=')
        encoding_dict[allele] = int(value)

    # Encode the dataframe
    for values in genotype_df.columns[3:]:
        genotype_df[values].replace(encoding_dict, inplace=True)

    # Save the resulting output file without headers
    genotype_df.to_csv(output_file, index=None, header=False)

    print(f"BIMBAM file saved to: {output_file}")

def add_genotype_subcommand(subparsers):
    parser = subparsers.add_parser("genotype", help="Process a genotype file.")
    parser.add_argument('genotype_file', help='Path to the genotype file (CSV)')
    parser.add_argument('alleles_file', help='Path to the alleles file (CSV)')
    parser.add_argument('encoding', help='Encoding scheme for the genotype data (e.g., "AA=0,AB=1,BB=2")')
    parser.add_argument('--na_encoding', default='NA', help='Encoding for missing values (default: NA)')
    parser.add_argument('--output-file', help='Path to the output BIMBAM file (CSV)')
    return subparsers


def rqtl2phenotype_to_bimbam(phenotype_file, num_rows, output_file=None):
    """
    Processes the rqtl2 phenotype file and converts it to BIMBAM format. 
    Args: 
        phenotype_file (str): Path to the phenotype file in CSV format.
        num_rows (int): Number of rows to process from the genotype file.
        output_file (str, optional): Path to the output BIMBAM file in CSV format.
        
    """
    # Load the input phenotype file
    phenotype_df = pd.read_csv(phenotype_file)

    # Check for the number of rows
    phenotype_df = phenotype_df.head(num_rows)

    # Check and ensure decimal places are at least 3
    def check_decimal_places(x):
        if isinstance(x, (int, float)):
            if len(str(x).split('.')[1]) < 3:
                return f"{x:.3f}"
            else:
                return x
        else:
            return x

    for values in phenotype_df.columns[1:]:
        phenotype_df[values] = phenotype_df[values].apply(check_decimal_places)

    phenotype_df = phenotype_df.iloc[:, 1:]

    # Save the resulting output file without headers
    phenotype_df.to_csv(output_file, index=None, header=False)

    print(f"BIMBAM file saved to: {output_file}")

def add_phenotype_subcommand(subparsers):
    parser = subparsers.add_parser("phenotype", help="Process a phenotype file.")
    parser.add_argument('phenotype_file', help='Path to the phenotype file (CSV)')
    parser.add_argument('--num_rows', type=int, default=None, help='Number of rows to process {NB; make sure the number of rows correspond to the number of column values in genotype file} (default: all)')
    parser.add_argument('--na_encoding', default='NA', help='Encoding for missing values (default: NA)')
    parser.add_argument('--output-file', help='Path to the output BIMBAM file (CSV)')
    return subparsers


def main():
    """Entry point to the script!"""
    parser = argparse.ArgumentParser(description='Convert RQTL2 files to BIMBAM format')
    subparsers = parser.add_subparsers(
        help="Use --help with each command below to see what it does.",
        title="Available Commands",
        required=True,
        dest="command")
    add_genotype_subcommand(subparsers)
    add_phenotype_subcommand(subparsers)
    args = parser.parse_args()
        
    ## Call the functions according to the subcommand 
    if args.command == "genotype":
        rqtl2genotype_to_bimbam(args.genotype_file,
                                    args.alleles_file,
                                    args.encoding,
                                    args.output_file)
    elif args.command == "phenotype":
        rqtl2phenotype_to_bimbam(args.phenotype_file, args.num_rows, args.output_file)
    else: 
        print("Invalid command. Please use 'genotype' or 'phenotype'.") 
        return 1
    return 0 

if __name__ == "__main__":
    sys.exit(main())
