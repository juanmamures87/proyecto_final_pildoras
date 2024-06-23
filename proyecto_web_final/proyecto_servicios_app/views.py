from django.shortcuts import render
from proyecto_servicios_app.models import Servicios

def servicios (request):
    servicios_app = Servicios.objects.all()
    contexto = {'servicios_app': servicios_app}
    return render(request, 'proyecto_servicios_app/servicios.html', contexto)
