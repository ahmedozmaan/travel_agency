# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in travel_agency/__init__.py
from travel_agency import __version__ as version

setup(
	name='travel_agency',
	version=version,
	description='Travel Agency Management System',
	author='rasiin',
	author_email='info@rasiin.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
