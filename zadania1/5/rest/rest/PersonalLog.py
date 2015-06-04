from rest_framework.views import View
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
 
log = [
	{ "category":"update", "person":"all", "time":1433412540, "content":"testtesttest test test!" },
	{ "category":"inna", "person":"nikt", "time":1433412898, "content":"eeeeeeeeeee test test!" },
	{ "category":"news", "person":"all", "time":1433412540, "content":"testtesttest news test!" },
	{ "category":"update", "person":"all", "time":1433412777, "content":"testtesttest time test!" },
	{ "category":"update", "person":"john", "time":1433412540, "content":"testtesttest test john" }
]
 
class Log(View):
	@api_view(['GET'])
	def get(self, request):
		print "Log matched"
		return Response(log)

class LogByCategory(View):
	@api_view(['GET'])
	def get(self, request, cat):
		print "LogByCategory matched"
		return Response([ x for x in log if x["category"] == cat ])
 
class LogByPerson(View):
	@api_view(['GET'])
	def get(self, request, per):
		print "LogByPerson matched"
		return Response([ x for x in log if x["person"] == per ])

class LogByTime(View):
	@api_view(['GET'])
	def get(self, request, time):
		print "LogByTime matched"
		return Response([ x for x in log if x["time"] == time])