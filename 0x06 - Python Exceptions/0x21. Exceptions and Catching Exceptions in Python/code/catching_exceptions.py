#!/usr/bin/python

# import module sys to get the type of exception

import sys

random_list = ['a', 0, 2]

for entry in random_list:
	try:
		print("The entry is", entry)

		r = 1/int(entry)

		break
	except:
		print("Oops! ", sys.exc_info()[0], " occured.")
		print("Next entry.")
		print()

print("The reciprocal of ", entry, " is ", r)