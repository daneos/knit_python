from django.conf.urls import patterns, include, url
from PersonalLog import *

urlpatterns = patterns("",
	url(r"^$", Log.as_view()),
	url(r"^category/(?P<cat>[A-Za-z0-9]*)$", LogByCategory.as_view()),
	url(r"^person/(?P<per>[A-Za-z0-9]*)$", LogByPerson.as_view()),
	url(r"^time/(?P<time>[0-9]*)$", LogByTime.as_view()),
)
