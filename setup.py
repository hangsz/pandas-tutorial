#!/usr/bin/env python
# coding: utf-8

import setuptools
from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='pandas-tutorial',
    version='0.1.0',
    author='hangsz',
    author_email='zhenhang.sun@outlook.com',
    url='https://github.com/hangsz/pandas-tutorial',
    description=u'pandas tutorial',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        'raft-python==0.1.3',
        'pandas==2.2.1'
    ]
)