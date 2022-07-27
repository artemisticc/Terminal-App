from distutils.core import setup
from setuptools import find_packages
import os

# # Optional project description in README.md:
# current_directory = os.path.dirname(os.path.abspath(__file__))

# try:
#     with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
#         long_description = f.read()
# except Exception:
#     long_description = ''
setup(

# Project name: 
name="Catalogue",

# Packages to include in the distribution: 
packages=find_packages(','),

# Project version number:
version="1",

# List a license for the project, eg. MIT License
license="MIT Licence",

# Short description of your library: 
description="Terminal app for T1A3",

# # Long description of your library: 
# long_description=long_description,
# long_description_content_type='text/markdown',

# Your name: 
author="Nicole Hall",

# Your email address:
author_email="12760@coderacademy.edu.au",

# Link to your github repository or website: 
url="https://github.com/artemisticc/Terminal-App",

# Download Link from where the project can be downloaded from:
download_url="https://github.com/artemisticc/Terminal-App",

# List of keywords: 
keywords=[],

# List project dependencies: 
install_requires=[
    "<simple_term_menu>",
    "<termcolor>",
    "<tabulate>",
    "<art>",
    "<pandas>",
    "<colorama>"
],
)