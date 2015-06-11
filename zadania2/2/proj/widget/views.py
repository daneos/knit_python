from django.shortcuts import render_to_response
from widget.models import Device

def show(request, device):
	""" Widok widgetu - pokazuje atrybuty urzadzenia """
	d = Device(device)

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
	context = { 'device': device, 'attrs': attrs, 'connection': d.attList['connectionStatus'] }
	return render_to_response('widget/show.template.html', context)