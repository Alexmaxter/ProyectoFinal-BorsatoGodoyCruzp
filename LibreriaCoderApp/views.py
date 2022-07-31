from asyncio.windows_events import NULL
from django.contrib.auth.models import User
from random import randrange, choice
from django.shortcuts import render
from BlogApp.forms import FormularioBusqueda
from BlogApp.models import Post


def inicio(request):

    users = User.objects.all()
    ultimo_post= None
    total_post = Post.objects.count()
    post_random = []

    def aleatorio():
        opciones = list(Post.objects.all())
        cantidad = 3
        while cantidad > 0:
            r = choice(opciones)
            post_random.append(r)
            opciones.remove(r)
            cantidad-=1
            yield r

    gen = aleatorio()

    try:
        while total_post  > 0:
            next(gen)
    except:
        ...
        total_post -=1


    try:
        ultimo_post=Post.objects.latest('id')

    except :
        ...
        
    
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
    "post_random":post_random,
    "formulario_busqueda": formulario_busqueda,
    "total_usuarios":total_usuarios})

