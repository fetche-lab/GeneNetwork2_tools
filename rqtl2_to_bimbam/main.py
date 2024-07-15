# main.py
"""
main.py file for the rqtl2_to_bimbam package.
"""
import argparse
import pandas as pd

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description='Convert RQTL2 files to BIMBAM format')
    parser.add_argument('--genotype_file', required=True, help='Path to the genotype file (CSV)')
    parser.add_argument('--phenotype_file', required=True, help='Path to the phenotype file (CSV)')
    parser.add_argument('--alleles_file', required=True, help='Path to the alleles file (CSV)')
    parser.add_argument('--num_rows', type=int, default=None, help='Number of rows to process {NB; make sure the number of rows correspond to the number of column values in genotype file} (default: all)')
    parser.add_argument('--output_file', required=True, help='Path to the output BIMBAM file (CSV)')
    parser.add_argument('--encoding', required=True, help='Encoding scheme for the genotype data (e.g., "AA=0,AB=1,BB=2")')
    parser.add_argument('--na_encoding', default='NA', help='Encoding for missing values (default: NA)')

    # Parse the arguments
    args = parser.parse_args()

    # Call the appropriate conversion function based on the command-line arguments
    if args.genotype_file and args.alleles_file:
        convert_rqtl2geno_to_bimbam(args.genotype_file, args.alleles_file, args.output_file, args.encoding, args.na_encoding)
    elif args.phenotype_file:
        convert_rqlt2pheno_to_bimbam(args.phenotype_file, args.num_rows, args.output_file, args.na_encoding)
    else:
        print("Error: Please provide either a genotype file or a phenotype file.")

def convert_rqtl2geno_to_bimbam(genotype_file, alleles_file, output_file, encoding, na_encoding):
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

def convert_rqlt2pheno_to_bimbam(phenotype_file, num_rows, output_file, na_encoding):
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

if __name__ == "__main__":
    main()