from .views import blog, crear_post, buscar_post, post, editar_post, eliminar_post, comentar
from django.urls import path

urlpatterns = [
    path("", blog, name='blog'),
    path('crear_post/', crear_post, name='crear_post'),
    path('buscar_post/', buscar_post, name='buscar_post'),
    path('post/<int:id>/', post, name='post'),
    path('editar_post/<int:id>/', editar_post, name='editar_post'),
    path('eliminar/<int:id>/', eliminar_post, name='eliminar_post'),
    path('comentar/<int:id>/', comentar, name='comentar'),
]
