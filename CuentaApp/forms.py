# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class FormularioRegistro(UserCreationForm):
    
#     nombre_usuario=forms.CharField(label='Usuario', max_length=30)
#     email= forms.EmailField()
#     clave_1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
#     clave_2= forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    
#     class Meta:
#         model= User
#         fields = ['nombre_usuario', 'email', 'clave_1', 'clave_2']
#         help_texts = { key: '' for key in fields }    
        
        
# class FormularioEditarUsuario(forms.Form):
#     email= forms.EmailField(required=False)
#     nombre=forms.CharField(label='Nombre', max_length=30, required=False)
#     last_name=forms.CharField(label='last_name', max_length=30, required=False)
#     clave_1= forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
#     clave_2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput, required=False)
#     avatar = forms.ImageField(required=False)
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User

class FormularioInicioSesion(AuthenticationForm):
    username = UsernameField(label=False,widget=forms.TextInput(attrs={"autofocus": True,'class': 'form-control','placeholder': 'Nombre de usuario'}))
    password = forms.CharField(label=False, strip=False, widget=forms.PasswordInput(attrs={"autocomplete": "current-password",'class': 'form-control','placeholder': 'Contraseña'}),)

    def __init__(self, *args, **kwargs):
        super(FormularioInicioSesion, self).__init__(*args, **kwargs)

class FormularioRegistro(UserCreationForm):
    
    username=forms.CharField(label=False, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombres de usuario'}))
    email= forms.EmailField(label=False,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email'}))
    password1= forms.CharField(label=False, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Contraseña'}))
    password2= forms.CharField(label=False, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Contraseña'}))
    
    
    class Meta:
        model= User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = { key: '' for key in fields }    
        
        
class FormularioEditarPerfil(forms.Form):
    email= forms.EmailField(label=False, required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email'}))
    first_name=forms.CharField(label=False, max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre'}))
    last_name=forms.CharField(label=False, max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Apellido'}))
    descripcion=forms.CharField(label=False,required=False , widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Descripción'}))
    password1= forms.CharField(label=False, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Contraseña'}), required=False)
    password2= forms.CharField(label=False, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Repetir contraseña'}), required=False)
    avatar = forms.ImageField(required=False)