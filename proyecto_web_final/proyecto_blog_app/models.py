from django.db import models

class Blog (models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    imagen = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"
        
    def __str__(self) -> str:
        return self.titulo
