from django.conf.urls import patterns, include, url
import rest.PersonalLog

urlpatterns = patterns("",
	url(r"^$", rest.PersonalLog.home),
	url(r"^category/(?P<cat>[A-Za-z0-9]*)$", rest.PersonalLog.getByCategory),
	url(r"^person/(?P<per>[A-Za-z0-9]*)$", rest.PersonalLog.getByPerson),
	url(r"^time/(?P<time>[0-9]*)$", rest.PersonalLog.getByTime),
)
