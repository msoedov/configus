# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = """
A unified way how to describe a spec of environment paramaters
required for the application runtime.
Support override params from command line or env file.
"""

setup(
    name="configus",
    version="0.1.0",
    description="Configus - declarative spec for configuration",
    license="MIT",
    author="Alex Myasoedov",
    author_email="msoedov@gmail.com",
    packages=['configus'],
    install_requires=['trafaret'],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ]
)
