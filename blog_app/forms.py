from django import forms
from .models import Autor, Categoria, Articulo

class FormularioAutor(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'email', 'biografia']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'biografia': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class FormularioArticulo(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'autor', 'categoria']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }

class FormularioBusqueda(forms.Form):
    consulta = forms.CharField(label='Buscar artículo', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del artículo...'}))
