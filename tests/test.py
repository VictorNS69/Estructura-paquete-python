#!/usr/bin/env python3

import unittest
from setuptools.command.test import test as TestCommand
from division import Division 

class MyTests(unittest.TestCase):
	def test_div0_1(self):
		with self.assertRaises(ZeroDivisionError):
			Division(1, 0)

	def test_div0_2(self):
		with self.assertRaises(ZeroDivisionError):
			Division(-1, 0)

	def test_div0_3(self):
		with self.assertRaises(ZeroDivisionError):
			Division(0, 0)

	def test_nan_1(self):
		with self.assertRaises(TypeError):
			Division("a", 1)

	def test_nan_2(self):
		with self.assertRaises(TypeError):
			Division(1, "b")

	def test_nan_3(self):
		with self.assertRaises(TypeError):
			Division("a", "b")

	def test_ok_1(self):
		self.assertEqual(Division(1, 2).result(), 0.5)

	def test_ok_2(self):
		self.assertEqual(Division(-1, 2).result(), -0.5)

	def test_ok_3(self):
		self.assertEqual(Division(0, 2).result(), 0.0)

if __name__ == '__main__':
	unittest.main()

