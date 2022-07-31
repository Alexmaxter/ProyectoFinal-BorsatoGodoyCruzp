from django.db import models
from django.contrib.auth.models import User


class MasDatosUsuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField(User,max_length=280, null=True, blank=True)
    last_name=models.CharField(User,max_length=280, null=True, blank=True)
    descripcion = models.CharField(max_length=280, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

    def __str__(self):
        return f"""
            {self.user}
            {self.descripcion}
            {self.avatar}"""
