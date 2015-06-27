from google.appengine.ext import ndb

class Choice(ndb.Model):
	""" Klasa odpowiedzi w ankiecie """
	choice = ndb.StringProperty()
	votes = ndb.IntegerProperty()

class Poll(ndb.Model):
	""" Klasa ankiety """
	question = ndb.StringProperty()
	date = ndb.DateTimeProperty(auto_now_add=True)
	total_votes = ndb.IntegerProperty()
	choices = ndb.StructuredProperty(Choice, repeated=True)

def ancestor():
	""" Zwraca klucz uzywany jako wspolny przodek wszystkich ankiet """
	return ndb.Key(Poll, 'polls')