#!/usr/bin/env python3

import math

class Division(object):
	def __init__(self, a, b):
		self.dividend = a
		self.divider = b
		if math.isnan(self.dividend) or math.isnan(self.divider):
			raise ValueError()
		if self.divider == 0:
			raise ZeroDivisionError()

	def result(self):
		return float(self.dividend)/self.divider

def main():
	try:
		print("Insert a:")
		a = int(input())
		print("Insert b:")
		b = int(input())
		aux = Division(a, b)
		print ("Result: " +str(aux.result()))

	except ZeroDivisionError:
		print("Can not be divided by 0")

	except ValueError:
		print("Insert only digits")

if __name__ == "__main__":
	main()
