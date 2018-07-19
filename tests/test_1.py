#!/usr/bin/env python3

import pytest
import src.division as d

class Test(object):
	def test_div0_1(self, capsys):
		with pytest.raises(ZeroDivisionError):
			d.Division(1, 0)

	def test_div0_2(self, capsys):
		with pytest.raises(ZeroDivisionError):
			d.Division(-1, 0)

	def test_div0_3(self, capsys):
		with pytest.raises(ZeroDivisionError):
			d.Division(0, 0)

	def test_nan_1(self, capsys):
		with pytest.raises(TypeError):
			d.Division("a", 1)

	def test_nan_2(self, capsys):
		with pytest.raises(TypeError):
			d.Division(1, "b")

	def test_nan_3(self, capsys):
		with pytest.raises(TypeError):
			d.Division("a", "b")

	def test_ok_1(self, capsys):
		assert d.Division(1, 2).result() == 0.5

	def test_ok_2(self, capsys):
		assert d.Division(-1, 2).result() == -0.5

	def test_ok_3(self, capsys):
		assert d.Division(0, 2).result() == 0.0


