
from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    reaonly_fields = ('creado','actualizado','id')
    list_display = ('titulo','autor', 'creado')
    list_filter = ('autor','creado')

admin.site.register(Post, PostAdmin)