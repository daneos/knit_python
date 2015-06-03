#!/usr/bin/env python

import sys
import itertools
import re

regexp = r"([a-z])\1"	# podwojne wystapienie znaku

def A(L):
	""" Funkcja realizujaca podpunkt A:
		Dwie identyczne litery obok siebie """
	for i in itertools.ifilter(lambda x: re.search(regexp, x), L):
		print i.capitalize()

def B(L):
	""" Funkcja realizujaca podpunkt B:
		Grupowanie wg. dlugosci elementow """
	s = {}
	for i in L:
		try:
			s[len(i)] += (i,)	# nowa krotka z dodanym elementem
		except KeyError:
			s[len(i)] = (i,)	# nie ma klucza, musze utworzyc
	print s

#------------------------------------------------------------------------------
if __name__ == "__main__":
	list1 = ['orange', 'apple', 'banana']
	list2 = ('carrot', 'potato', 'lettuce')
	list3 = {'milk', 'sugar', 'butter', 'flour'}
	list_full = list1 + list(list2) + list(list3)
	
	try:
		locals()[sys.argv[1].upper()](list_full)			# wywolanie odpowiedniej funkcji z argumentow
	except Exception:										# nie chce przechwytywac KeyboardInterrupt, etc.
		print "Uzycie: %s <A/B>" % sys.argv[0]				# blad argumentow