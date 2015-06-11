from django.conf.urls import include, url

urlpatterns = [
	url(r'^(?P<device>.+)', 'widget.views.show'),
]