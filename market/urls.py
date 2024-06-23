from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('index', views.index, name='index'),
    path('listarProductos', views.listarProductos, name='listarProductos'),
    path('listarCarrito', views.listarCarrito, name='listarCarrito'),
    path('listarCategoria', views.listarCategoria, name='listarCategoria'),
    path('anadirProductoForm', views.anadirProductoForm, name='anadirProductoForm'),
    path('anadirCategoria', views.anadirCategoria, name='anadirCategoria'),
    path('anadirCarrito', views.anadirCarrito, name='anadirCarrito'),
    path('buscarCategoria/<int:pk>', views.buscarCategoria, name='buscarCategoria'),
    path('editarProducto/<int:pk>', views.editarProducto, name='editarProducto'),
]