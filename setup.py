# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in havenir_erpnext_iot/__init__.py
from havenir_erpnext_iot import __version__ as version

setup(
	name='havenir_erpnext_iot',
	version=version,
	description='IOT app using MQTT',
	author='Havenir',
	author_email='info@havenir.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
