from django.shortcuts import render_to_response
from widget.models import Device

def show(request, device):
	""" Widok widgetu - pokazuje atrybuty urzadzenia
		Jesli jest przekazany parametr GET ?action=update
		zwraca tylko tabele z danymi. Jesli nie, zwraca pelna strone """
	d = Device(device, True)

	if not d.error:
		attrs = []
		for i in range(1, d.attList['attCount']):
			attrs.append({
				'Name':		d.attList['attribute' + str(i-1)],
				'Scalar':	d.attList['attScalar' + str(i-1)],
				'Value':	d.attList['attValue' + str(i-1)],
				'Writable':	d.attList['attWritable' + str(i-1)],
				'Plotable':	d.attList['attPlotable' + str(i-1)],
				'Numeric':	d.attList['isNumeric' + str(i-1)],
				'Desc':		d.attList['attDesc' + str(i-1)]
			})
		context = { 'device': device, 'attrs': attrs, 'connection': d.attList['connectionStatus'], 'url': request.path }
	else:
		context = { 'device': device, 'connection': 'UNKNOWN', 'error': d.error, 'url': request.path }
	
	if request.GET.get('action', None) == 'update':
		return render_to_response('widget/content.template.html', context)	# jesli wywolany z AJAXa przesyla tylko content
	else:
		return render_to_response('widget/full.template.html', context)		# jesli nie, rowniez skrypty i style