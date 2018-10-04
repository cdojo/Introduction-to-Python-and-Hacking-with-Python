#!/usr/bin/python

x = 10

def example1():
	print x


def example2():
	x += 5


def example3():
	global x
	x += 5

	print x


def example4():
	globalx = x
	print globalx
	
	globalx += 5
	print globalx


def example5():
	print x
	return x


example1()
# example2()
# example3()
# example4()
# print example5() + 15