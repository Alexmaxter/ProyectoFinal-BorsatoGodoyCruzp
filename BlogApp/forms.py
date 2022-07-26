from django import forms
from ckeditor.fields import RichTextFormField


class FormularioPost(forms.Form):
    titulo = forms.CharField(max_length=30)
    subtitulo = forms.CharField(max_length=50)
    contenido = RichTextFormField()
    imagen = forms.ImageField()

class FormularioBusqueda(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)
