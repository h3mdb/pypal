#!/usr/bin/env python3

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    setup(
        name='Pypal',
        author='Daniel Turner',
        version='0.0.1a',
        packages=['pypal'],
        package_dir={'pypal': 'src'},
        description='Python port of Pipal for password analytics',
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/h3mdb/pypal",
        #package_data={'pypal': ['lists/']},
        #include_package_data=True,
        install_requires=[
            'altair==3.1.0',
            'matplotlib==3.4.2',
            'fuzzyset==0.0.19',
            'nltk==3.4.5',
            'pandas==1.2.5',
            'tqdm==4.32.2',
            'vega-datasets==0.7.0',
            'cython==0.29.14',
            ],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: POSIX",
            "Operating System :: MacOS",
            ],
        )
