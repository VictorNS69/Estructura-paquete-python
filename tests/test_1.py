

__AUTHOR__ = "Victor Nieves Sanchez"
__COPYRIGHT__ = "Copyright 2018, Victor Nieves Sanchez"
__CREDITS__ = ["Victor Nieves Sanchez"]
__LICENSE__ = "GPL"
__VERSION__ = "1.0.0"
__PYTHON__= "3.6.4"
__EMAIL__ = "vnievess@gmail.com"


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

	def test_void(self, capsys):
		with pytest.raises(TypeError):
			d.Division("",2)

	def test_none(self, capsys):
		with pytest.raises(TypeError):
			d.Division(None, 2)


