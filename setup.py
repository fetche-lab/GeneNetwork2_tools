from setuptools import setup, find_packages

setup(
    name='rqtl2_to_bimbam',
    version='1.0.0',
    description='Convert RQTL2 files to BIMBAM format',
    author='Felix Lisso',
    author_email='flisso434@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'rqtl2Pheno-to-bimbam = rqtl2_to_bimbam.rqtl2Pheno-to-bimbamPheno:convert_rqlt2pheno_to_bimbam',
            'rqtl2Geno-to-bimbam = rqtl2_to_bimbam.rqtl2Geno-to-bimbamGeno:convert_rqlt2geno_to_bimbam',
        ],
    },
)