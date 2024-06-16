from django.contrib import admin
from .models import Servicios

class ServiciosAdmin (admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('id','titulo','contenido','imagen','created','updated')
    
admin.site.register(Servicios,ServiciosAdmin)