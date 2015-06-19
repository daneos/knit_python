import json

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.serializers import serialize
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from SOAPpy import SOAPBuilder

from polls.models import Choice, Poll
from polls.serializers import PollSerializer, ChoiceSerializer

def index(request):
	""" Strona glowna - lista ankiet """
	latest_poll_list = Poll.objects.all().order_by('-date')		# sortowanie od najnowszego
	req_format = request.GET.get('format', None)
	
	if req_format:
		serialized = [ PollSerializer(p, detail=False) for p in latest_poll_list ]
		if req_format == 'json':
			return HttpResponse(json.dumps(serialized),
								content_type='application/json')
		if req_format == 'soap':
			soap = SOAPBuilder(args=serialized)
			return HttpResponse(soap.build(),
								content_type='text/plain') #content_type='application/soap+xml')
	else:
		return render_to_response('polls/index.template.html', {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
	""" Widok szczegolowy ankiety - formularz glosowania """
	p = get_object_or_404(Poll, pk=poll_id)
	req_format = request.GET.get('format', None)
	
	if req_format:
		serialized = PollSerializer(p)
		if req_format == 'json':
			return HttpResponse(json.dumps(serialized),
								content_type='application/json')
		if req_format == 'soap':
			soap = SOAPBuilder(args=serialized)
			return HttpResponse(soap.build(),
								content_type='text/plain') #content_type='application/soap+xml')
	else:
		context = {'poll': p}
		context.update(csrf(request))		# ochrona przed CSRF
		return render_to_response('polls/detail.template.html', context)

@csrf_exempt								# inaczej nie dziala json ani soap, wymaga csrf, wyrzuca blad niezaleznie od wejscia
def vote(request, poll_id):
	""" Obsluga glosow """
	if request.method == 'POST':
		p = get_object_or_404(Poll, pk=poll_id)
		req_format = request.GET.get('format', None)

		if req_format:
			if req_format == 'json':
				try:
					ch = json.loads(request.body)['choice']			# numer wybranej opcji z JSON
				except Exception as e:
					return HttpResponse(json.dumps('Invalid JSON input.'),
										content_type='application/json')
			if req_format == 'soap':
				pass
		else:
			ch = request.POST['choice']								# numer wybranej opcji z POST
			
		try:
			selected_choice = p.choice_set.get(pk=ch)				# pobieranie modelu opcji na podstwie numeru z requestu
		except (KeyError, Choice.DoesNotExist):
			
			if req_format:
				if req_format == 'json':
					return HttpResponse(json.dumps('Invalid choice or no choice.'),
										content_type='application/json')
				if req_format == 'soap':
					pass
			else:
				context = {
					'poll': p,
					'error_message': 'Invalid choice or no choice.',
				}
				context.update(csrf(request))	# ochrona przed CSRF
				return render_to_response('polls/detail.template.html', context)

		selected_choice.votes += 1
		selected_choice.save()			# zapis oddanego glosu
		return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))

	else:
		return detail(request, poll_id)		# jesli metoda nie jest POST zwraca widok ankiety

def results(request, poll_id):
	""" Widok wynikow ankiety """
	p = get_object_or_404(Poll, pk=poll_id)
	req_format = request.GET.get('format', None)

	if req_format:
		serialized = PollSerializer(p, results=True)
		if req_format == 'json':
			return HttpResponse(json.dumps(serialized),
								content_type='application/json')
		if req_format == 'soap':
			soap = SOAPBuilder(args=serialized)
			return HttpResponse(soap.build(),
								content_type='text/plain') #content_type='application/soap+xml')
	else:
		return render_to_response('polls/results.template.html', {'poll': p})