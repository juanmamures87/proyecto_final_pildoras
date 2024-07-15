from django.urls import path
from proyecto_inicio_app.views import home,tienda,blog,contacto

urlpatterns = [
    path('', home, name='home'),
    path('tienda/', tienda, name='tienda'),
    path('contacto/', contacto, name='contacto'),
]