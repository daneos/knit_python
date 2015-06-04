from rest_framework.views import View
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from time import time
from re import findall
 
log = [
	{ "category":["update"], "person":["all"], "time":1433412540, "content":"testtesttest test test!" },
	{ "category":["inna"], "person":["nikt"], "time":1433412898, "content":"eeeeeeeeeee test test!" },
	{ "category":["news"], "person":["all"], "time":1433412540, "content":"testtesttest news test!" },
	{ "category":["update"], "person":["all"], "time":1433412777, "content":"testtesttest time test!" },
	{ "category":["update"], "person":["john"], "time":1433412540, "content":"testtesttest test john" }
]

parse_category = r"#(\S*)"
parse_person = r"@(\S*)"

@api_view(["GET", "POST"])
def home(request):
	""" GET: Zwraca wszystkie wpisy
		POST: Dodaje nowy wpis """
	if request.method == "GET":
		return Response(sorted(log, key=lambda x: x["time"], reverse=True)[:10])	# sortowanie i zwracanie 10 wpisow
	elif request.method == "POST":
		log.append({
			"category":	findall(parse_category, request.data) or ["none"],
			"person":	findall(parse_person, request.data) or ["none"],
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
		return Response([ x for x in log if x["time"] == int(time) ])