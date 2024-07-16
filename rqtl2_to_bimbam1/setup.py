"""
setup.py file for the rqtl2_to_bimbam package.
"""

from setuptools import setup, find_packages

setup(
    name='rqtl2_to_bimbam',
    version='1.0.0',
    description='Convert RQTL2 files to BIMBAM format',
    author='Felix Lisso and Frederick Muriithi',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'Rqtl2-BimBam = rqtl2_to_bimbam.rqtl2-to-bimbam:main'
        ],
    },
)
