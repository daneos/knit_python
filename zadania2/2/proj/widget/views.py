from django.shortcuts import render_to_response
from widget.models import Device

def show(request, device):
	""" Widok widgetu - pokazuje atrybuty urzadzenia """
	d = Device(device)

	for i in range(0, d.attList.attCount-1):
		pass