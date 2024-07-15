from django.urls import path
from proyecto_blog_app.views import blog

urlpatterns = [
    path('', blog, name='blog'),
]