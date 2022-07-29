from django.shortcuts import render,redirect
from BlogApp.models import Post, Categoria
from BlogApp.forms import FormularioPost, FormularioBusqueda
from django.contrib.auth.decorators import login_required

from CuentaApp.models import MasDatosUsuarios

def blog(request):

    posts=Post.objects.all().order_by("-id")
    categoria = Categoria.objects.all()



    return render(request, "BlogApp/blog.html",{'posts':posts,'categoria':categoria})


def categoria(request,categoria_id):

    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    
    return render(request, "BlogApp/categoria.html",{'categoria':categoria,'posts':posts})


@login_required
def crear_post(request):
    
    if request.method == "POST":
        
        formulario_post = FormularioPost(request.POST, request.FILES)

        if formulario_post.is_valid():
            
            informacion = formulario_post.cleaned_data


            post = Post(
                titulo = informacion['titulo'],
                subtitulo = informacion['subtitulo'],
                contenido = informacion['contenido'],
                imagen = informacion['imagen'],
            )

            post.autor = request.user
            post.save()

            return redirect('blog')
        
    else:
        formulario_post = FormularioPost()

    return render(request, 'BlogApp/crear_post.html', {'formulario_post': formulario_post})


def post(request, id):

    post = Post.objects.get(id=id)
    return render(request, "BlogApp/post.html", {"post": post})


def buscar_post(request):

    

    consulta = request.GET.get("titulo")
    

    if consulta:
        listado_post = Post.objects.filter(titulo__icontains=consulta)

    else:
        listado_post = Post.objects.all().order_by("-id")

    formulario_busqueda = FormularioBusqueda()
    
    return render(request, "BlogApp/buscar_post.html" , {"listado_post": listado_post, "formulario_busqueda": formulario_busqueda})

# @login_required
# def editar_post(request, id):

#     post = Post.objects.get(id=id)
    
#     formulario_editar_post = FormularioPost(initial={'titulo': post.titulo, 'subtitulo': post.subtitulo, 'contenido': post.contenido, 'autor': post.autor, 'creado': post.creado, 'imagen': post.imagen})
    
#     if request.method == 'POST':
#         formulario_editar_post = FormularioPost(request.POST, request.FILES)
#         if formulario_editar_post.is_valid():
#             post.titulo = formulario_editar_post.cleaned_data.get('titulo')
#             post.subtitulo = formulario_editar_post.cleaned_data.get('subtitulo')
#             post.contenido = formulario_editar_post.cleaned_data.get('contenido')
#             post.autor = formulario_editar_post.cleaned_data.get('autor')
#             post.creado = formulario_editar_post.cleaned_data.get('creado')
#             post.imagen = formulario_editar_post.cleaned_data.get('imagen')
            
#             post.save()
            
#             return redirect('buscar_post')
#         else:
#             return render(request, "BlogApp/editar_post.html", {"formulario_editar_post": formulario_editar_post, "post": post})
    
    
#     return render(request, "BlogApp/editar_post.html", {"formulario_editar_post": formulario_editar_post, "post": post})

@login_required
def editar_post(request, id):
    post = Post.objects.get(id=id)
    
    formulario_post = FormularioPost(initial={'titulo': post.titulo, 'subtitulo': post.subtitulo, 'contenido': post.contenido, 'autor': post.autor, 'creado': post.creado, 'imagen': post.imagen})
   
    if request.method == 'POST':
        form = FormularioPost(request.POST, request.FILES)

        if form.is_valid():
            post.titulo = form.cleaned_data.get('titulo')
            post.subtitulo = form.cleaned_data.get('subtitulo')
            post.contenido = form.cleaned_data.get('contenido')
            post.autor = form.cleaned_data.get('autor')
            post.creado = form.cleaned_data.get('creado')
            post.imagen = form.cleaned_data.get('imagen')
            post.save()
            
            return redirect('post')
        else:
            return render(request, "BlogApp/crear_post.html", {"formulario_post": formulario_post, "post": post})
    
    
    return render(request, "BlogApp/editar_post.html", {"formulario_post": formulario_post, "post": post})

@login_required
def eliminar_post(request, id):
    
    post = Post.objects.get(id=id)
    post.delete()
    
    return redirect('blog')

