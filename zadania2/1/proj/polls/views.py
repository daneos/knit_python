from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from polls.models import Choice, Poll

def index(request):
	""" Strona glowna - lista ankiet """
	latest_poll_list = Poll.objects.all().order_by('-date')
	return render_to_response('polls/index.template.html', {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
	""" Widok  szczegolowy ankiety - formularz glosowania """
	p = get_object_or_404(Poll, pk=poll_id)
	context = {'poll': p}
	context.update(csrf(request))
	return render_to_response('polls/detail.template.html', context)

def vote(request, poll_id):
	""" Obsluga glosow """
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		context = {
			'poll': p,
			'error_message': "Nie wybrales zadnej opcji",
		}
		context.update(csrf(request))
		return render_to_response('polls/detail.template.html', context)
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))

def results(request, poll_id):
	""" Widok wynikow ankiety """
	p = get_object_or_404(Poll, pk=poll_id)	
	return render_to_response('polls/results.template.html', {'poll': p})