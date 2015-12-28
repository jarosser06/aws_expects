#!/usr/bin/env python

import ast
import re
from setuptools import setup, find_packages

DEPENDENCIES = [
    'boto3==1.2.2',
    'expects',
]

TESTS_REQUIRE = []


def package_meta():
    """Read __init__.py for global package metadata.
    Do this without importing the package.
    """
    _version_re = re.compile(r'__version__\s+=\s+(.*)')
    _url_re = re.compile(r'__url__\s+=\s+(.*)')
    _license_re = re.compile(r'__license__\s+=\s+(.*)')

    with open('aws/__init__.py', 'rb') as ffinit:
        initcontent = ffinit.read()
        version = str(ast.literal_eval(_version_re.search(
            initcontent.decode('utf-8')).group(1)))
        url = str(ast.literal_eval(_url_re.search(
            initcontent.decode('utf-8')).group(1)))
        licencia = str(ast.literal_eval(_license_re.search(
            initcontent.decode('utf-8')).group(1)))
    return {
        'version': version,
        'license': licencia,
        'url': url,
    }

_lu_meta = package_meta()

setup(
    name='aws_expects',
    description='Custom Matchers for the Python Expects Testing Framework',
    keywords='aws cloudformation',
    version=_lu_meta['version'],
    tests_require=TESTS_REQUIRE,
    install_requires=DEPENDENCIES,
    packages=find_packages(exclude=['tests']),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
    ],
    license=_lu_meta['license'],
    author="Jim Rosser",
    maintainer_email="jarosser06@gmail.com",
    url=_lu_meta['url'],
)
