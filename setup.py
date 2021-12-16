#!/usr/bin/env python
# coding: utf-8
from yudzuki import __version__
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

long_description = ""
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read().replace('\r\n', '\n')

requirements = ""
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read()

setup(
    name='yudzuki.py',
    version=__version__,
    license='MIT',
    description='An API Wrapper for Yudzuki API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='midorichaan',
    author_email='furandorusukaret.jp@gmail.com',
    url='https://github.com/LunaProject-Discord/yudzuki.py',
    install_requires=requirements,
    packages=find_packages(),
    keywords='yudzuki.py',
)
