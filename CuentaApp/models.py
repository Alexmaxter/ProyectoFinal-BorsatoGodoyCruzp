from pyexpat import model
from django.db import models
from django.contrib.auth.models import User



class MasDatosUsuarios (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=280, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return self.user
    
    def __str__(self):
        return self.avatar

    def __str__(self):
        return self.descripcion