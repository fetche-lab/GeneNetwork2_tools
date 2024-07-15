"""
setup.py file for the rqtl2_to_bimbam package.
"""

from setuptools import setup, find_packages

setup(
    name='rqtl2_to_bimbam',
    version='1.0.0',
    description='Convert RQTL2 files to BIMBAM format',
    author='Felix Lisso',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'Geno-Rqlt2Bimbam = rqtl2_to_bimbam.main:convert_rqtl2geno_to_bimbam',
            'Pheno-Rqtl2Bimbam = rqtl2_to_bimbam.main:convert_rqlt2pheno_to_bimbam'
        ],
    },
)
