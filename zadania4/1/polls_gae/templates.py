import os
from google.appengine.ext.webapp import template

def render(name, context):
	""" Renderuje szablon """
	path = os.path.join(os.path.dirname(__file__), name)
	return template.render(path, context)