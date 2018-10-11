#!/bin/usr/python

try:
	a = int(input("Enter a positive Integer: "))

	if a <= 0:
		raise ValueError("That is not a positive integer!")
except ValueError as ve:
	print(ve)
finally:
	print("End of the program")