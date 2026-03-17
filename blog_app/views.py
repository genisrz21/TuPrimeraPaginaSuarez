from django.shortcuts import render, redirect
from .models import Autor, Categoria, Articulo
from .forms import FormularioAutor, FormularioCategoria, FormularioArticulo, FormularioBusqueda
from django.contrib import messages

def inicio(request):
    articulos = Articulo.objects.all().order_by('-fecha_publicacion')
    return render(request, 'blog_app/home.html', {'articulos': articulos})

def agregar_autor(request):
    if request.method == 'POST':
        form = FormularioAutor(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor creado exitosamente.')
            return redirect('inicio')
    else:
        form = FormularioAutor()
    return render(request, 'blog_app/add_author.html', {'form': form})

def agregar_categoria(request):
    if request.method == 'POST':
        form = FormularioCategoria(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente.')
            return redirect('inicio')
    else:
        form = FormularioCategoria()
    return render(request, 'blog_app/add_category.html', {'form': form})

def agregar_articulo(request):
    if request.method == 'POST':
        form = FormularioArticulo(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Artículo creado exitosamente.')
            return redirect('inicio')
    else:
        form = FormularioArticulo()
    return render(request, 'blog_app/add_article.html', {'form': form})

def buscar_articulos(request):
    consulta = request.GET.get('consulta', '')
    articulos = []
    if consulta:
        articulos = Articulo.objects.filter(titulo__icontains=consulta)
    
    form = FormularioBusqueda(initial={'consulta': consulta})
    return render(request, 'blog_app/search_results.html', {'form': form, 'articulos': articulos, 'consulta': consulta})

