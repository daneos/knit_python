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
		return Response(log)
	elif request.method == "POST":
		log.append({
			"category":	findall(parse_category, request.data) or ["none"],
			"person":	findall(parse_person, request.data) or ["none"],
			"time":		int(time()),
			"content":	request.data
			})
		return Response(status=status.HTTP_201_CREATED)

@api_view(['GET'])
def getByCategory(request, cat):
	""" Zwraca wpisy tylko z jednej kategorii """
	if request.method == "GET":
		return Response([ x for x in log if x["category"].__contains__(cat) ])
 
@api_view(['GET'])
def getByPerson(request, per):
	""" Zwraca wpisy przefiltrowane po osobie """
	if request.method == "GET":
		return Response([ x for x in log if x["person"].__contains__(per) ])

@api_view(['GET'])
def getByTime(request, time):
	""" Zwraca wpisy wedlug czasu dodania """
	if request.method == "GET":
		return Response([ x for x in log if x["time"] == int(time) ])