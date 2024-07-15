from django.shortcuts import render
from proyecto_blog_app.models import Blog

def blog (request):
    return render(request, 'proyecto_blog_app/blog.html')
