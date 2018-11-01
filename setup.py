#!/usr/bin/env python
import os
import re
import sys
from codecs import open

from setuptools import find_packages
from setuptools import setup


os.chdir(os.path.abspath(os.path.dirname(__file__)))

with open("analytical/__init__.py", "r") as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
    ).group(1)

if not version:
    raise RuntimeError("Cannot find version information")

with open("README.rst", "r", "utf-8") as f:
    description = f.read()

setup(
    name="analytical",
    version=version,
    description="Python Server Side Analytics",
    long_description=description,
    author="Read the Docs, Inc.",
    author_email="dev@readthedocs.org",
    url="http://github.com/rtfd/analytical",
    packages=find_packages(exclude=["tests"]),
    install_requires=["requests", "six", "user-agents"],
    license="MIT",
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    keywords="analytics donottrack privacy",
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ),
    test_suite="tests",
)
