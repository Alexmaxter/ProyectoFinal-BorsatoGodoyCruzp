from django.urls import path
from .views import blog, categoria, crear_post, buscar_post, post, editar_post, eliminar_post

urlpatterns = [
    path("", blog, name='blog'),
    path('categoria/<categoria_id>/', categoria, name='categoria'),
    path('crear_post/', crear_post, name='crear_post'),
    path('buscar_post/', buscar_post, name='buscar_post'),
    path('post/<int:id>/', post, name='post'),
    path('editar/<int:id>/', editar_post, name='editar_post'),
    path('eliminar/<int:id>/', eliminar_post, name='eliminar_post'),
]