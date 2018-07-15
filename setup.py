#!/usr/bin/env python3

__AUTHOR__ = "Victor Nieves Sanchez"
__COPYRIGHT__ = "Copyright 2018, Victor Nieves Sanchez"
__CREDITS__ = ["Victor Nieves Sanchez"]
__LICENSE__ = "GPL"
__VERSION__ = "1.0.0"
__PYTHON__= "3.6.4"
__EMAIL__ = "vnievess@gmail.com"

from setuptools import setup
from setuptools.command.test import test as TestCommand

setup(name="Pruebas test",
	version=__VERSION__,
	description='Pruebas sobre el uso de test y el setup en python',
	author=__AUTHOR__,
	author_email=__EMAIL__,
	url='https://github.com/VictorNS69',
	license=__LICENSE__,
	classifiers=['Programming Language :: Python :: 3.5'],
	packages=['tests'],)
