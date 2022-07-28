from sre_constants import CATEGORY_LINEBREAK
from django import forms
from ckeditor.fields import RichTextFormField

from BlogApp.models import Categoria



class FormularioPost(forms.Form):


    titulo = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Título'}),label="")
    subtitulo = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Subtítulo'}),label="")
    contenido = RichTextFormField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Contenido'}),label="")
    imagen = forms.ImageField(label="")
    
    class Meta:
        autor = ('autor',)

class FormularioBusqueda(forms.Form):
    titulo = forms.CharField(max_length=30, required=False,label=False,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Buscar por título'}))
