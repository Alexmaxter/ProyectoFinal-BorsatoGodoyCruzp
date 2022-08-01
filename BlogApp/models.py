
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db import models

class Post(models.Model):
    
    titulo=models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    contenido= RichTextField(blank=True, null=True)
    imagen=models.ImageField(upload_to='blog',null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):

        return f"{self.titulo}"