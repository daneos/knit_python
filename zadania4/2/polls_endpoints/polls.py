package = 'Polls'

import endpoints
from google.appengine.ext import ndb
from protorpc import remote

from models import Poll, Choice

@endpoints.api(name='polls', version='v1', description='Polls API')
class Polls(remote.Service):
	""" Klasa API ankiet """

	@Poll.method(path='polls', http_method='POST', name='polls.create', request_fields=('question', 'choices'))
	def create(self, poll):
		""" Tworzenie ankiety, uzupelnia wymagane pola """
		for c in poll.choices:
			c.id = ndb.Key(Choice, c.choice).urlsafe()
			c.votes = 0
		poll.total_votes = 0
		poll.put()
		return poll

	@Poll.query_method(path='polls', http_method='GET', name='polls.list')
	def list(self, query):
		""" Lista ankiet """
		return query.order(-Poll.date)

	@Poll.method(request_fields=('id',), path='polls/{id}', http_method='GET', name='polls.get')
	def get(self, poll):
		""" Pojedyncza ankieta """
  		if not poll.from_datastore:
  			raise endpoints.NotFoundException('Poll not found.')
  		return poll

  	@Poll.method(path='polls/{id}', http_method='PUT', name='polls.vote', request_fields=('id',))
  	def vote(self, poll, choice):
  		""" Glosowanie w ankiecie """
  		pass

app = endpoints.api_server([Polls], restricted=False)