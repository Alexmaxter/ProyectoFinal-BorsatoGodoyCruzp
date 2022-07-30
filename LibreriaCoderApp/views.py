from collections import  UserList
from django.contrib.auth.models import User

from django.shortcuts import render
from BlogApp.forms import FormularioBusqueda
from BlogApp.models import Post


def inicio(request):

    users = User.objects.all()
    ultimo_post=Post.objects.latest('id')
    # categoria = Categoria.objects.all()

    total_usuarios=User.objects.count()


    consulta = request.GET.get("titulo")

    if consulta:
        listado_post = Post.objects.filter(titulo__icontains=consulta)

    else:   
        listado_post = Post.objects.all()

    formulario_busqueda = FormularioBusqueda()
    
    
    return render(request, "inicio.html", {"users":users,"ultimo_post": ultimo_post,
    "listado_post": listado_post,
    "formulario_busqueda": formulario_busqueda,
    "total_usuarios":total_usuarios})

