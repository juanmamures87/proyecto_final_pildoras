from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, 'proyecto_inicio_app/home.html')

def tienda (request):
    return render(request, 'proyecto_inicio_app/tienda.html')

def blog (request):
    return render(request, 'proyecto_inicio_app/blog.html')

def contacto (request):
    return render(request, 'proyecto_inicio_app/contacto.html')