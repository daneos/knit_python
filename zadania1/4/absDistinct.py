#!/usr/bin/env python

def absDistinct(A):
	""" Ilosc unikalnych wartosci bezwzglednych elementow listy """
	return len(set( [abs(x) for x in A] ))		# uzywam zbioru do usuniecia powtarzajacych sie elementow

#------------------------------------------------------------------------------
if __name__ == "__main__":
	A = [ -5, -3, -1, 0, 3, 6 ]
	print absDistinct(A)