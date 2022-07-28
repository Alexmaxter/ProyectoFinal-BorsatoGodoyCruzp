
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nombre

class Post(models.Model):
    
    titulo=models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    contenido= RichTextField(blank=True, null=True)
    imagen=models.ImageField(upload_to='blog',null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return f"{self.titulo} {self.autor}"

