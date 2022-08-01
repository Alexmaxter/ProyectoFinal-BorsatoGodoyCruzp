
from django.contrib import admin
from .models import Post, Comentario


class PostAdmin(admin.ModelAdmin):

    reaonly_fields = ('creado', 'actualizado', 'id')
    list_display = ('imagenAdmin', 'titulo', 'autor', 'creado')
    list_filter = ('autor', 'creado')


class ComentarioAdmin(admin.ModelAdmin):

    reaonly_fields = ('creado', 'ientrada')
    list_display = ('autor', 'creado')
    list_filter = ('autor', 'creado')


admin.site.register(Post, PostAdmin)
admin.site.register(Comentario, ComentarioAdmin)
