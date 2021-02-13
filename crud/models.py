from django.db import models
"""
Autor (nombre, email)
Articulo (autores, titulo, contenido)
"""

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    public = models.BooleanField()
    # Usado cuando cree el registro me guarda la fecha, solo se hara una vez para este registro
    created_at = models.DateTimeField(auto_now_add=True)
    # Usado cuando actualice el registro me guarda la fecha, solo se hara a partir del momento que se actualice
    update_at = models.DateTimeField(auto_now_add=True)


class Author(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    # Usado cuando cree el registro me guarda la fecha, solo se hara una vez para este registro
    created_at = models.DateTimeField(auto_now_add=True)
    # Usado cuando actualice el registro me guarda la fecha, solo se hara a partir del momento que se actualice
    update_at = models.DateTimeField(auto_now_add=True)
