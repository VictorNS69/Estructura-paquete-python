#!/usr/bin/env python3

__AUTHOR__ = "Victor Nieves Sanchez"
__COPYRIGHT__ = "Copyright 2018, Victor Nieves Sanchez"
__CREDITS__ = ["Victor Nieves Sanchez"]
__LICENSE__ = "GPL"
__VERSION__ = "1.0.0"
__PYTHON__= "3.6.4"
__EMAIL__ = "vnievess@gmail.com"

from distutils.core import setup
from setuptools.command.test import test as TestCommand

def readme():
	with open("README.md") as file:
		return file.read()

setup(name="Ejemplo de paquete python",
	version=__VERSION__,
	description='Pruebas sobre el uso de tests, setup y paquetes en python',
	long_description=readme(),
	author=__AUTHOR__,
	author_email=__EMAIL__,
	url='https://github.com/VictorNS69',
	license=__LICENSE__,
	classifiers=['Programming Language :: Python :: 3.5'],
	packages=['src', 'tests'],
	test_suite='nose.collector',
	tests_require=['nose'],)
