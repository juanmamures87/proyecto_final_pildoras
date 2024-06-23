from django.urls import path
from proyecto_servicios_app.views import servicios

urlpatterns = [
    path('', servicios, name='servicios'),
]