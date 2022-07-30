
from django.contrib import admin
from .models import Post


# class CategoriaAdmin(admin.ModelAdmin):
#     readonly_fields = ('creado','actualizado')


class PostAdmin(admin.ModelAdmin):
    reaonly_fields = ('creado','actualizado','id')

# admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)