from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar-autor/', views.agregar_autor, name='agregar_autor'),
    path('agregar-categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('agregar-articulo/', views.agregar_articulo, name='agregar_articulo'),
    path('buscar/', views.buscar_articulos, name='buscar_articulos'),
]
