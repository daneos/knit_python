from django.conf.urls import patterns, include, url
import rest.PersonalLog

urlpatterns = patterns("",
	url(r"^$",						rest.PersonalLog.home),
	url(r"^category/(?P<cat>.*)$",	rest.PersonalLog.byCategory),
	url(r"^person/(?P<per>.*)$",	rest.PersonalLog.byPerson),
	url(r"^time/(?P<time>[0-9]*)$",	rest.PersonalLog.byTime),
)
