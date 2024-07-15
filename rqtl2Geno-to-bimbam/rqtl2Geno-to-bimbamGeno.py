import pandas as pd
import argparse

def convert_rqtl2geno_to_bimbam():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description='Convert RQTL2 genotype files to BIMBAM format')
    parser.add_argument('--genotype_file', required=True, help='Path to the genotype file (CSV)')
    parser.add_argument('--alleles_file', required=True, help='Path to the alleles file {The file headers should be minor and major repsectively} (CSV)')
    parser.add_argument('--output_file', required=True, help='Path to the output BIMBAM file (CSV)')
    parser.add_argument('--encoding', required=True, help='Encoding scheme for the genotype data (e.g., "AA=0,AB=1,BB=2")')
    parser.add_argument('--na_encoding', default='NA', help='Encoding for missing values (default: NA)')


    # Parse the arguments
    args = parser.parse_args()

    # Load the input files
    genotype_df = pd.read_csv(args.genotype_file)
    alleles_df = pd.read_csv(args.alleles_file)
    #phenotype_df = pd.read_csv(args.phenotype_file)

    # Add columns from alleles_df to genotype_df
    genotype_df.insert(1, 'minor', alleles_df['minor'])
    genotype_df.insert(2, 'major', alleles_df['major'])

    # Parse the encoding scheme
    encoding_dict = {}
    for pair in args.encoding.split(','):
        allele, value = pair.split('=')
        encoding_dict[allele] = int(value)

    # Encode the dataframe
    for values in genotype_df.columns[3:]:
        genotype_df[values].replace(encoding_dict, inplace=True)


    # Save the resulting output file without headers
    genotype_df.to_csv(args.output_file, index=None, header=False)

    print(f"BIMBAM file saved to: {args.output_file}")

if __name__ == "__main__":
    convert_rqtl2geno_to_bimbam()