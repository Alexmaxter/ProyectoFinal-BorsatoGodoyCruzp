from sre_constants import CATEGORY_LINEBREAK
from django import forms
from ckeditor.fields import RichTextFormField

from BlogApp.models import Categoria



class FormularioPost(forms.Form):


    titulo = forms.CharField(max_length=30)
    subtitulo = forms.CharField(max_length=50)
    contenido = RichTextFormField()
    imagen = forms.ImageField()
    
    class Meta:
        autor = ('autor',)

class FormularioBusqueda(forms.Form):
    titulo = forms.CharField(max_length=30, required=False,label=False)
