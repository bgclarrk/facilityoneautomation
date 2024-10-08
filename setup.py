# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open("README.rst") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="sample",
    version="0.1.0",
    description="Sample automation project for FacilityONE",
    long_description=readme,
    author="Brian Clark",
    author_email="bcglarrk@live.com",
    url="https://github.com/bgclarrk/facilityoneautomation",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
)
