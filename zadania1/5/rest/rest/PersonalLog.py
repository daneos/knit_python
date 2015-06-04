from rest_framework.views import View
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from time import time
from re import findall
 
log = []

parse_category = r"\B#(\S*)"
parse_person = r"\B@(\S*)"		# \B blokuje rozpoznawanie czesci np. adresu e-mail jako osoby

@api_view(["GET", "POST"])
def home(request):
	""" GET: Zwraca wszystkie wpisy
		POST: Dodaje nowy wpis """
	if request.method == "GET":
		return Response(sorted(log, key=lambda x: x["time"], reverse=True)[:10])	# sortowanie i zwracanie 10 wpisow
	elif request.method == "POST":
		log.append({
			"category":	findall(parse_category, request.data) or ["none"],		# moze byc kilka kategorii w jednym wpisie
			"person":	findall(parse_person, request.data) or ["none"],		# j.w.
			"time":		int(time()),
			"content":	request.data
			})
		return Response(status=status.HTTP_201_CREATED)

@api_view(['GET'])
def byCategory(request, cat):
	""" Zwraca wpisy tylko z jednej kategorii """
	if request.method == "GET":
		r = [ x for x in log if x["category"].__contains__(cat) ]		# wybieranie wpisow na podstwaie kategorii
		r.sort(key=lambda x: x["time"], reverse=True)					# sortowanie wg. czasu dodania
		return Response(r[:10])				# zwracam tylko 10 ostatnich wpisow
 
@api_view(['GET'])
def byPerson(request, per):
	""" Zwraca wpisy przefiltrowane po osobie """
	if request.method == "GET":
		r = [ x for x in log if x["person"].__contains__(per) ]			# wybieranie wpisow na podstawie osoby
		r.sort(key=lambda x: x["time"], reverse=True)					# sortowanie wg. czasu dodania
		return Response(r[:10])				# zwracam tylko 10 ostatnich wpisow

@api_view(['GET'])
def byTime(request, time):
	""" Zwraca wpisy wedlug czasu dodania """
	if request.method == "GET":
		return Response([ x for x in log if x["time"] == int(time) ][:10])	# zwracam tylko 10 ostatnich wpisów