from django.contrib import admin
from .models import MasDatosUsuarios

class MasDatosUsuariosAdmin(admin.ModelAdmin):
    reaonly_fields = ('user','descripcion','first_name','last_name')
    list_display = ('user','descripcion','first_name','last_name')

    def __str__(self):
        return "user"

    

admin.site.register(MasDatosUsuarios,MasDatosUsuariosAdmin)   