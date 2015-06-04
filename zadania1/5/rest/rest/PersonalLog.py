from rest_framework.views import View
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from time import time
 
log = [
	{ "category":"update", "person":"all", "time":1433412540, "content":"testtesttest test test!" },
	{ "category":"inna", "person":"nikt", "time":1433412898, "content":"eeeeeeeeeee test test!" },
	{ "category":"news", "person":"all", "time":1433412540, "content":"testtesttest news test!" },
	{ "category":"update", "person":"all", "time":1433412777, "content":"testtesttest time test!" },
	{ "category":"update", "person":"john", "time":1433412540, "content":"testtesttest test john" }
]

@api_view(["GET", "POST"])
def home(request):
	if request.method == "GET":
		print "Log matched"
		return Response(log)
	elif request.method == "POST":
		log.append({
			"category":	"test",
			"person":	"test2",
			"time":		int(time()),
			"content":	request.data
			})
		return Response(status=status.HTTP_201_CREATED)

@api_view(['GET'])
def getByCategory(request, cat):
	if request.method == "GET":
		return Response([ x for x in log if x["category"] == cat ])
 
@api_view(['GET'])
def getByPerson(request, per):
	if request.method == "GET":
		return Response([ x for x in log if x["person"] == per ])

@api_view(['GET'])
def getByTime(request, time):
	if request.method == "GET":
		return Response([ x for x in log if x["time"] == int(time) ])