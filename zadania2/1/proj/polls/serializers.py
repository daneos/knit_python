def PollSerializer(p, detail=True, results=False):
	data = {}
	data['id'] = p.id
	data['question'] = p.question
	data['date'] = str(p.date)
	if detail or results:
		data['choices'] = [ ChoiceSerializer(c, results) for c in p.choice_set.all()]
	if results:
		data['total_votes'] = p.total_votes()
	return data

def ChoiceSerializer(c, results=False):
	data = {}
	data['id'] = c.id
	data['choice'] = c.choice
	if results:
		data['votes'] = c.votes
	return data