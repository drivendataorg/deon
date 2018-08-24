#!/usr/bin/env python

import setuptools
from setuptools import setup

setup(
    name='deon',
    url="https://github.com/drivendataorg/deon",
    version='0.1',
    author="DrivenData",
    author_email="info@drivendata.org",

    description='Deon, a Data Science Ethics Checklist Generator',
    long_description=open('README.md').read(),

    license='MIT',
    packages=setuptools.find_packages(),

    install_requires=[],

    entry_points={
        'console_scripts': [
            'deon=deon.ethics_checklist:main',
        ]
    },

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
