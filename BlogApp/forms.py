from ckeditor.fields import RichTextFormField
from django import forms


from BlogApp.models import Comment


class FormularioPost(forms.Form):

    titulo = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Título'}), label="")
    subtitulo = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Subtítulo'}), label="")
    contenido = RichTextFormField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Contenido'}), label="")
    imagen = forms.ImageField(label="", required=False)

    class Meta:

        autor = ('autor',)


class FormularioBusqueda(forms.Form):

    titulo = forms.CharField(max_length=30, required=False, label=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Buscar por título'}))


class CommentForm(forms.ModelForm):
    
    body = RichTextFormField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Contenido'}), label="")
    class Meta:
        model = Comment
        fields = ('body',)