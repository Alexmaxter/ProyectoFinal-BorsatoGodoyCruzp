from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from .models import MasDatosUsuarios
from django.contrib.auth.decorators import login_required
from .forms import FormularioInicioSesion, FormularioRegistro, FormularioEditarPerfil
from BlogApp.models import Post

# def iniciar_sesion(request):
    
#     if request.method == 'POST':
#         formulario_inicio = AuthenticationForm(request, data=request.POST)
        
#         if formulario_inicio.is_valid():

#             nombre_usuario = formulario_inicio.cleaned_data.get('nombre_usuario')
#             clave= formulario_inicio.cleaned_data.get('clave')
            
#             usuario=authenticate(nombre_usuario=nombre_usuario, clave_1=clave)
        
#             if usuario is not None:
            
#                 django_login (request, usuario)
#                 return render (request, 'inicio.html', {})
            
#             else:
            
#                 return render(request, 'CuentaApp/iniciar_sesion.html', {'formulario_inicio': formulario_inicio})
        
#         else:
        
#             return render(request, 'CuentaApp/iniciar_sesion.html',  {'formulario_inicio': formulario_inicio})
            
    
#     formulario_inicio = AuthenticationForm()
#     return render(request, 'CuentaApp/iniciar_sesion.html',  {'formulario_inicio': formulario_inicio})


# def registro(request):
    
#     if request.method == 'POST':

#         formulario_registro = FormularioRegistro(request.POST)
    
#         if formulario_registro.is_valid():

#             formulario_registro.save()
#             return render (request, 'inicio.html', {})

        
#         else:

#             return render(request, 'CuentaApp/registro.html', {'formulario_registro': formulario_registro})
    
#     formulario_registro=FormularioRegistro()
    
#     return render (request, 'CuentaApp/registro.html', {'formulario_registro': formulario_registro})


# @login_required

# def perfil(request):
#     return render (request, 'CuentaApp/perfil.html')

# @login_required

# def editar_perfil(request):
    
#     usuario = request.usuario
#     usuario_extra = Usuario.objects.get_or_create(usuario=usuario)
    
#     if request.method == 'POST':
#         formulario_editar= FormularioEditarUsuario(request.POST, request.FILES)
#         if formulario_editar.is_valid():
#             data = formulario_editar.cleaned_data
#             usuario.first_name = data.get('first_name') if data.get('first_name') else  usuario.first_name
#             usuario.last_name = data.get('last_name') if data.get('last_name') else  usuario.last_name
#             usuario.email = data.get('email') if data.get('email') else usuario.email
#             usuario_extra.avatar = data.get('avatar') if data.get('avatar') else usuario_extra.avatar
            
#             if data.get('password1') and data.get('password1') == data.get('password2'):
#                 usuario.set_password(data.get('password1'))
            
#             usuario_extra.save()
#             usuario.save()
            
#             return redirect('perfil')
        
#         else:
#             return render(request, 'accounts/editar_perfil.html', {'form_edit':formulario_editar} )    
            
    
#     formulario_editar = FormularioEditarUsuario(
#         initial={
#             'email': usuario.email,
#             'nombre': usuario.nombre,
#             'last_name': usuario.last_name,
#             'avatar': usuario_extra.avatar,
#         }
#     )
             
#     return render (request, 'accounts/editar_perfil.html', {'form_edit':formulario_editar})



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
            return render (request, 'inicio.html', {})
        else:
            return render(request, 'CuentaApp/registro.html', {'formulario_registro': formulario_registro} )
    
    formulario_registro=FormularioRegistro()
    return render (request, 'CuentaApp/registro.html', {'formulario_registro': formulario_registro})

@login_required
def perfil(request):

    posts = Post.objects.all()
    
    return render (request, 'CuentaApp/perfil.html',{'posts':posts})

@login_required

def editar_perfil(request):
    
    user = request.user
    mas_datos_usuarios, _ = MasDatosUsuarios.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        form_edit= FormularioEditarPerfil(request.POST, request.FILES)
        if form_edit.is_valid():
            data = form_edit.cleaned_data
            user.first_name = data.get('first_name') if data.get('first_name') else user.first_name
            user.last_name = data.get('last_name') if data.get('last_name') else user.last_name
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
            'first_name': user.first_name,
            'last_name': user.last_name,
            'descripcion': mas_datos_usuarios.descripcion,
            'avatar': mas_datos_usuarios.avatar,
        }
    )

    return render (request, 'CuentaApp/editar_perfil.html', {'form_edit':form_edit})

def perfil_usuario(request, id):

    usuario = MasDatosUsuarios.objects.get(id=id)
    posts = Post.objects.all()

    return render (request, 'CuentaApp/perfil_usuario.html', {'usuario':usuario,"posts":posts})