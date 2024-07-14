# rqtl2_to_bimbam 

This is a Python program designed and written to convert `genotype files` and `phenotype files` from [Rqtl2 format](https://kbroman.org/qtl2/assets/vignettes/input_files.html) to [BIMBAM format](https://github.com/genetics-statistics/GEMMA/blob/master/doc/manual.pdf). These file formats are popular in most GeneNetwork analyses. 

# Installation 
All dependencies needed for this program are found in `requirements.txt`.
- To install the package, users can run the following command:
  ```bash
  pip install git+https://github.com/fetche-lab/GeneNetwork2_tools.git
  ```
# Running rqtl2_to_bimbam 
Once the tool is installed, the following are the commands one can run to convert genotype or phenotype files from rqtl2 format to bibam format 
- For converting the genotype file, run the following command:
  ```bash
  rqtl2Geno-to-bimbam --genotype_file genotype_input.csv --alleles_file allele_input.csv --encoding "a=0,b=1" --output_file genotype_bimbam.csv
  ```
- For converting the phenotype file, run the following command:
  ```bash
  rqtl2Pheno-to-bimbam --phenotype_file phenotype_input.csv --no_rows 30 --output_file phenotype_bimbam.csv 
  ```
 - To convert the genotype file, the `--genotype_file`, `-allele_file` and `--encoding` options are necessary as they provide the requirements for the bimbam format.
 - To convert the phenotype file, the `--no_rows` is important to specify the number of rows to be processed which should correspond to the number of column values in genotype file.
 - Optionally, for both, genotype and phenotype conversions, one can use the --na_encoding to format for the empty values. The default is 'NA'.
 - The `examples_files` folder contains example files for rqlt2 files and the corresponding bimbam files.
 - To get help, one can run the following option;
 - For genotype;
   ```bash
    rqtl2Geno-to-bimbam --help  
   ```
 - For phenotype;
   ```bash
    rqtl2Pheno-to-bimbam --help  
   ```
