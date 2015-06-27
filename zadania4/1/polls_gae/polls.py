import webapp2
from google.appengine.ext import ndb

from templates import render
from models import Poll, Choice, ancestor

class Home(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('Home page')

class Polls(webapp2.RequestHandler):
	def get(self, poll_id):
		poll = ndb.Key(urlsafe=poll_id).get()
		self.response.write(render('poll.html', { 'poll':poll }))

	def post(self, poll_id):
		pass

class Results(webapp2.RequestHandler):
	def get(self, poll_id):
		pass

class Creator(webapp2.RequestHandler):
	def get(self):
		self.response.write(render('create.html', {}))
	
	def post(self):
		new_poll = Poll(parent=ancestor())
		new_poll.question = self.request.get('question')
		new_poll.total_votes = 0
		new_poll.choices = [ Choice(choice=c, votes=0) for c in self.request.POST.getall('choice') if c ]
		new_poll.put()
		url = '/poll/' + new_poll.key.urlsafe()
		self.response.write('<pre>@ <a href="' + url + '">' + url + '</a></pre>')

app = webapp2.WSGIApplication(
	[
		('/', Home),
		('/poll/(.*)', Polls),
		('/results/(.*)', Results)
		('/create', Creator)
	],
debug=True)
