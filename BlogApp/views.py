from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from BlogApp.forms import FormularioComentario, FormularioPost, FormularioBusqueda
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from BlogApp.models import Comentario, Post
from django.urls import reverse


def blog(request):

    posts = Post.objects.all().order_by("-id")
    blog_vacio = posts.count()

    return render(request, "BlogApp/blog.html", {'posts': posts, 'blog_vacio': blog_vacio})


@login_required
def crear_post(request):

    if request.method == "POST":

        formulario_post = FormularioPost(request.POST, request.FILES)

        if formulario_post.is_valid():

            informacion = formulario_post.cleaned_data
            post = Post(
                titulo=informacion['titulo'],
                subtitulo=informacion['subtitulo'],
                contenido=informacion['contenido'],
                imagen=informacion['imagen'],)
            post.autor = request.user
            post.save()

            return redirect('blog')

    else:
        formulario_post = FormularioPost()

    return render(request, 'BlogApp/crear_post.html', {'formulario_post': formulario_post})


def post(request, id):

    post = Post.objects.get(id=id)
    comentarios = Comentario.objects.filter(post_id=id)
    cantidad_comentarios = Comentario.objects.filter(post_id=id).count()
    return render(request, "BlogApp/post.html", {"post": post, "comentarios": comentarios, "cantidad_comentarios": cantidad_comentarios})


def buscar_post(request):

    consulta = request.GET.get("titulo")

    if consulta:
        listado_post = Post.objects.filter(titulo__icontains=consulta)

    else:
        listado_post = Post.objects.all().order_by("-id")

    formulario_busqueda = FormularioBusqueda()

    return render(request, "BlogApp/buscar_post.html", {"listado_post": listado_post, "formulario_busqueda": formulario_busqueda})


@ login_required
def editar_post(request, id):

    post = Post.objects.get(id=id)

    if request.method == 'POST':

        edit_form = FormularioPost(request.POST, request.FILES)

        if edit_form.is_valid():

            form = edit_form.cleaned_data
            post.titulo = form.get('titulo') if form.get(
                'titulo') else post.titulo
            post.subtitulo = form.get('subtitulo') if form.get(
                'subtitulo') else post.subtitulo
            post.contenido = form.get('contenido') if form.get(
                'contenido') else post.contenido
            post.autor = form.get('autor') if form.get('autor') else post.autor
            post.creado = form.get('creado') if form.get(
                'creado') else post.creado
            post.imagen = form.get('imagen') if form.get(
                'imagen') else post.imagen
            post.save()

            return redirect('blog')

        else:

            return render(request, "BlogApp/editar_post.html", {"form": form, "post": post})

    form = FormularioPost(initial={'titulo': post.titulo, 'subtitulo': post.subtitulo,
                                   'contenido': post.contenido, 'autor': post.autor, 'creado': post.creado, 'imagen': post.imagen})

    return render(request, "BlogApp/editar_post.html", {"form": form, "post": post})


@ login_required
def eliminar_post(request, id):

    post = Post.objects.get(id=id)
    post.delete()

    return redirect('blog')
