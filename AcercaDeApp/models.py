from distutils.command.upload import upload
from tabnanny import verbose
from turtle import update
from django.db import models


class Empleado(models.Model):
    nombre=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=280)
    avatar=models.ImageField(upload_to='empleados')
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "empleado"
        verbose_name_plural = "empleados"

    def __str__(self):
        return self.nombre