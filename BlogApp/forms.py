from sre_constants import CATEGORY_LINEBREAK
from django import forms
from ckeditor.fields import RichTextFormField

from BlogApp.models import Categoria



class FormularioPost(forms.Form):

    # dic_categoria = {}

    # lista_categoria = []

    # for categoria in Categoria.objects.all():
    #     if categoria.nombre.nombre in dic_categoria:
    #         dic_categoria[categoria.nombre.nombre].append(categoria.nombre)
    #     else:
    #         dic_categoria[categoria.nombre.nombre] = [categoria.nombre]
    #     lista_categoria .append((categoria.nombre,categoria.nombre))

    titulo = forms.CharField(max_length=30)
    subtitulo = forms.CharField(max_length=50)
    contenido = RichTextFormField()
    imagen = forms.ImageField()
    #categoria = forms.ChoiceField(choices=(lista_categoria))
    
    class Meta:
        autor = ('autor',)

class FormularioBusqueda(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)
