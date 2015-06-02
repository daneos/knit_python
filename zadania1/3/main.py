#!/usr/bin/env python

import sys
import itertools
import re

list1 = ['orange', 'apple', 'banana']
list2 = ('carrot', 'potato', 'lettuce')
list3 = {'milk', 'sugar', 'butter', 'flour'}

regexp = r"([a-z])\1"	# podwojne wystapienie znaku

def A():
	""" Funkcja realizujaca podpunkt A:
		Dwie identyczne litery obok siebie """
	for i in list1 + list(list2) + list(list3):
		if re.search(regexp, i):
			print i.capitalize()

def B():
	""" Funkcja realizujaca podpunkt B:
		Grupowanie wg. dlugosci elementow """
	s = {}
	for i in list1 + list(list2) + list(list3):
		try:
			s[len(i)] += (i,)	# nowa krotka z dodanym elementem
		except KeyError:		# nie ma klucza, musze utworzyc
			s[len(i)] = (i,)
	print s

if __name__ == "__main__":
	try:
		locals()[sys.argv[1].upper()]()		# wywolanie odpowiedniej funkcji z argumentow
	except:					# blad argumentow
		print "Uzycie: %s <A/B>" % sys.argv[0]