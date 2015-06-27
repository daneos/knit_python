from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel, EndpointsAliasProperty

class Choice(EndpointsModel):
	""" Klasa odpowiedzi w ankiecie """
	id = ndb.StringProperty()
	choice = ndb.StringProperty()
	votes = ndb.IntegerProperty()

class Poll(EndpointsModel):
	""" Klasa ankiety """
	_message_fields_schema = ('id', 'question', 'date', 'choices', 'total_votes')

	question = ndb.StringProperty()
	date = ndb.DateTimeProperty(auto_now_add=True)
	total_votes = ndb.IntegerProperty()
	choices = ndb.StructuredProperty(Choice, repeated=True)

	def set_id(self, value):
		""" Pobiera ankiete z datastore, jesli istnieje """
		self.UpdateFromKey(ndb.Key(urlsafe=value))

	@EndpointsAliasProperty(setter=set_id, required=True)
	def id(self):
		""" Zwraca ID z klucza, aby zachowac zgodnosc z wersja REST """
		return self.key.urlsafe()

	def set_selected(self, value):
		self._selected = value

	@EndpointsAliasProperty(setter=set_selected, required=True)
	def selected_choice(self):
		return getattr(self, '_selected', None)