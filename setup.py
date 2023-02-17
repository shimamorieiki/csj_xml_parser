# Author: Eiki Shimamori <aifore.2270@gmail.com>
# Copyright (c) 2023-2024 Eiki Shimamori 
# License: MIT

from setuptools import setup

import csj_xml_parser

DESCRIPTION = "csj_xml_parser: parse CSJ(Corpus of Spontaneous Japanese) from XML"
NAME = 'csj_xml_parser'
AUTHOR = 'Eiki Shimamori'
AUTHOR_EMAIL = 'aifore.2270@gmail.com'
URL = 'https://github.com/shimamorieiki/csj_xml_parser'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/shimamorieiki/csj_xml_parser'
VERSION = csj_xml_parser.__version__
PYTHON_REQUIRES = ">=3.10"

# INSTALL_REQUIRES = [
#     'matplotlib>=3.3.4',
#     'seaborn>=0.11.0',
#     'numpy >=1.20.3',
#     'pandas>=1.2.4',
#     'matplotlib>=3.3.4',
#     'scipy>=1.6.3',
#     'scikit-learn>=0.24.2',
# ]

# EXTRAS_REQUIRE = {
#     'tutorial': [
#         'mlxtend>=0.18.0',
#         'xgboost>=1.4.2',
#     ]
# }

PACKAGES = [
    'csj_xml_parser'
]

CLASSIFIERS = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10'
]

with open('README.md', 'r') as fp:
    readme = fp.read()
# with open('CONTACT.txt', 'r') as fp:
#     contacts = fp.read()
# long_description = readme + '\n\n' + contacts

setup(name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
    #   long_description=long_description,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
    #   install_requires=INSTALL_REQUIRES,
    #   extras_require=EXTRAS_REQUIRE,
      packages=PACKAGES,
      classifiers=CLASSIFIERS
    )
