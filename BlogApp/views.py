from django.shortcuts import render,redirect
from BlogApp.models import Post, Categoria
from BlogApp.forms import FormularioPost, FormularioBusqueda
from django.contrib.auth.decorators import login_required

def blog(request):

    posts=Post.objects.all()
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

            post.save()

            return redirect('BlogApp/crear_post/')
        
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
        listado_post = Post.objects.all()

    form = FormularioBusqueda()
    
    return render(request, "BlogApp/buscar_post.html", {"listado_post": listado_post, "form": form})
