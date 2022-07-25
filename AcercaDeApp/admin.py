from django.contrib import admin
from .models import Empleado


class EmpleadoAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')

admin.site.register(Empleado, EmpleadoAdmin)
