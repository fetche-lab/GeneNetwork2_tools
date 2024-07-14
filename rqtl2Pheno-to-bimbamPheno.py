## import pandas and argparse libraries 
import pandas as pd 
import argparse

def convert_rqlt2pheno_to_bimbam():
    # Set up the argument parser 
    parser = argparse.ArgumentParser(description='Convert RQTL2 phenotype files to BIMBAM format')
    parser.add_argument('--phenotype_file', required=True, help='Path to the phenotype file (CSV)')
    parser.add_argument('--num_rows', type=int, default=None, help='Number of rows to process (default: all)')
    parser.add_argument('--output_file', required=True, help='Path to the output BIMBAM file (CSV)')
    parser.add_argument('--na_encoding', default='NA', help='Encoding for missing values (default: NA)')

    # Parse the arguments
    args = parser.parse_args()

    # Load in the input phenotype file 
    phenotype_df = pd.read_csv(args.phenotype_file)

    # Check for the number of rows 
    phenotype_df = phenotype_df.head(args.num_rows)

    # Check and ensure decimal places are at least 3 
    ## create a function for this 
    def check_decimal_places(x):
        if isinstance(x, (int, float)): 
            if len(str(x).split('.')[1]) < 3:
                return f"{x:.3f}"
            else:
                return x
        else:
            return x 
        
    ## apply it to the values in the file 
    for values in phenotype_df.columns[1:]: 
        phenotype_df[values] = phenotype_df[values].apply(check_decimal_places)
    
    ## exclude the first column 
    phenotype_df = phenotype_df.iloc[:, 1:] 

    # Save the resulting output file without headers
    phenotype_df.to_csv(args.output_file, index=None, header=False)

    print(f"BIMBAM file saved to: {args.output_file}")

if __name__ == "__main__":
    convert_rqlt2pheno_to_bimbam()




