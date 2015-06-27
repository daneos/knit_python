import webapp2
from google.appengine.ext import ndb

from templates import render
from models import Poll, Choice, ancestor

def get_or_404(instance, key):
	""" Pobiera obiekt lub rzuca wyjatek jesli obiekt nie istnieje """
	obj = None
	try:
		obj = ndb.Key(urlsafe=key).get()
		if not obj: raise Exception
	except Exception:
		instance.abort(404)
	return obj

class Home(webapp2.RequestHandler):
	""" Widok strony glownej - lista ankiet """
	def get(self):
		query = Poll.query(ancestor=ancestor()).order(-Poll.date)
		polls = query.fetch()
		self.response.write(render('home.html', { 'latest_poll_list':polls }))

class Polls(webapp2.RequestHandler):
	""" Widok ankiety """
	def get(self, poll_id):
		poll = get_or_404(self, poll_id)
		self.response.write(render('poll.html', { 'poll':poll }))

	def post(self, poll_id):
		ch = self.request.POST.get('choice')
		poll = get_or_404(self, poll_id)
		selected_choice = None
		for c in poll.choices:
			if c.id == ch:
				selected_choice = c
		if not selected_choice:
			error = 'Invalid choice or no choice'
			self.response.write(render('poll.html', { 'poll':poll, 'error_message':error }))
			return
		selected_choice.votes += 1
		poll.total_votes += 1
		poll.put()
		return webapp2.redirect('/results/' + poll_id)

class Results(webapp2.RequestHandler):
	""" Widok wynikow """
	def get(self, poll_id):
		poll = get_or_404(self, poll_id)
		self.response.write(render('results.html', { 'poll':poll }))

class Creator(webapp2.RequestHandler):
	""" Widok tworzenia nowej ankiety """
	def get(self):
		self.response.write(render('create.html', {}))
	
	def post(self):
		new_poll = Poll(parent=ancestor())
		new_poll.question = self.request.get('question')
		new_poll.total_votes = 0
		new_poll.choices = [ Choice(id=ndb.Key(Choice,c).urlsafe(), choice=c, votes=0) for c in self.request.POST.getall('choice') if c ]
		new_poll.put()
		url = '/poll/' + new_poll.key.urlsafe()
		self.response.write('<pre>@ <a href="' + url + '">' + url + '</a></pre>')

app = webapp2.WSGIApplication(
	[
		('/', Home),
		('/poll/(.*)', Polls),
		('/results/(.*)', Results),
		('/create', Creator)
	],
debug=True)
