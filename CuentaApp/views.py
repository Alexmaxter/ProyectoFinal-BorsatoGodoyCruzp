from re import S
from tkinter import Image
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from .models import MasDatosUsuarios
from django.contrib.auth.decorators import login_required
from .forms import FormularioInicioSesion, FormularioRegistro, FormularioEditarPerfil
from BlogApp.models import Post
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.models import User

def iniciar_sesion(request):
    if request.method == 'POST':
        form_login = FormularioInicioSesion(request, data=request.POST)
        
        if form_login.is_valid():
            username = form_login.cleaned_data.get('username')
            password= form_login.cleaned_data.get('password')
            
            user=authenticate(username=username, password=password)
        
            if user is not None:
                django_login (request, user)
                
                return redirect('inicio')
                return render (request, 'CuentaApp/iniciar_sesion.html', {})
            else:
                return render(request, 'CuentaApp/iniciar_sesion.html', {'form_login': form_login})
        else:
            return render(request, 'CuentaApp/iniciar_sesion.html', {'form_login': form_login})
            
    
    form_login = FormularioInicioSesion()
    return render(request, 'CuentaApp/iniciar_sesion.html', {'form_login': form_login})


def registro(request):


    if request.method == 'POST':
        formulario_registro = FormularioRegistro(request.POST)
        
        
        if formulario_registro.is_valid():
            
            formulario_registro.save()

            return redirect('iniciar_sesion')
        else:
            return render(request, 'CuentaApp/registro.html', {'formulario_registro': formulario_registro} )

    
    formulario_registro=FormularioRegistro()

  
    
    return render (request, 'CuentaApp/registro.html', {'formulario_registro': formulario_registro})

@login_required
def perfil(request):

    posts = Post.objects.filter(autor_id=request.user.id)

    usuario = None
    masdatosusuarios = None
    try:
        masdatosusuarios = MasDatosUsuarios.objects.all()
    except:
        usuario = User.objects.get(id=id)

    return render (request, 'CuentaApp/perfil.html',{'posts':posts,'usuario':usuario,'masdatosusuarios':masdatosusuarios})

@login_required

def editar_perfil(request):
    
    user = request.user
    mas_datos_usuarios, _ = MasDatosUsuarios.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        form_edit= FormularioEditarPerfil(request.POST, request.FILES)
        if form_edit.is_valid():
            data = form_edit.cleaned_data
            mas_datos_usuarios.first_name = data.get('first_name') if data.get('first_name') else mas_datos_usuarios.first_name
            mas_datos_usuarios.last_name = data.get('last_name') if data.get('last_name') else mas_datos_usuarios.last_name
            user.email = data.get('email') if data.get('email') else user.email
            mas_datos_usuarios.descripcion = data.get('descripcion') if data.get('descripcion') else mas_datos_usuarios.descripcion
            mas_datos_usuarios.avatar = data.get('avatar') if data.get('avatar') else mas_datos_usuarios.avatar
            
            if data.get('password1') and data.get('password1') == data.get('password2'):
                user.set_password(data.get('password1'))
            
            user.save()
            mas_datos_usuarios.save()
            
            return redirect('perfil')
        
        else:
            return render(request, 'CuentaApp/editar_perfil.html', {'form_edit':form_edit} )    
            
    
    form_edit = FormularioEditarPerfil(
        initial={
            'email': user.email,
            'nombre': mas_datos_usuarios.first_name,
            'apellido': mas_datos_usuarios.last_name,
            'descripcion': mas_datos_usuarios.descripcion,
            'avatar': mas_datos_usuarios.avatar,
        }
    )

    return render (request, 'CuentaApp/editar_perfil.html', {'form_edit':form_edit})

def perfil_usuario(request, id):

    posts = Post.objects.filter(autor=id)
    usuario = None
    masdatosusuarios = None
    try:
        masdatosusuarios = MasDatosUsuarios.objects.get(user=id)
    except:
        usuario = User.objects.get(id=id)
        

    return render (request, 'CuentaApp/perfil_usuario.html', {"posts":posts,"usuario":usuario,"masdatosusuarios":masdatosusuarios})

class ChangePasswordView(PasswordChangeView):
    template_name = 'CuentaApp/cambiar_contrasegna.html'
    succes_url = '/CuentaApp/perfil'
    