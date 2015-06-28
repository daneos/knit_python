package = 'Polls'

import endpoints
from google.appengine.ext import ndb
from protorpc import remote

from models import Poll, Choice

@endpoints.api(name='polls', version='v1')
class Polls(remote.Service):
	""" System ankiet: Endpoints API """

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

	@Poll.method(path='polls/{id}', http_method='GET', name='polls.get', request_fields=('id',))
	def get(self, poll):
		""" Pojedyncza ankieta """
		if not poll.from_datastore:
			raise endpoints.NotFoundException('Poll not found.')
		return poll

	@Poll.method(path='polls/{id}', http_method='PUT', name='polls.vote', request_fields=('id', 'selected_choice'))
	def vote(self, poll):
		""" Glosowanie w ankiecie """
		if not poll.from_datastore:
			raise endpoints.NotFoundException('Poll not found.')
		exists = False
		for c in poll.choices:
			if c.id == poll.selected_choice:
				c.votes += 1
				exists = True
		if not exists:
			raise endpoints.NotFoundException('Choice not foud.')
		poll.total_votes += 1
		poll.put()
		return poll

app = endpoints.api_server([Polls], restricted=False)