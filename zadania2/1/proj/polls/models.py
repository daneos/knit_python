from django.db import models

class Poll(models.Model):
	""" Klasa ankiety """
	question = models.CharField(max_length=200)
	date = models.DateTimeField()
	
	def __unicode__(self):
		""" Reprezentacja tekstowa ankiety """
		return self.question

	def total_votes(self):
		""" Liczba wszystkich glosow w ankiecie """
		t = 0
		for c in self.choice_set.all():
			t += c.votes
		return t


class Choice(models.Model):
	""" Klasa odpowiedzi w ankiecie """
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
	
	def __unicode__(self):
		""" Reprezentacja tekstowa odpowiedzi """
		return self.choice

	def percentage(self):
		""" Procentowa ilosc glosow na odpowiedz """
		total = self.poll.total_votes()
		if total == 0: return 0
		return (float(self.votes) / float(total)) * 100.