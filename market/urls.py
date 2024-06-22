from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('index', views.index, name='index'),
    path('listarProductos', views.listarProductos, name='listarProductos'),
    path('listarCarrito', views.listarCarrito, name='listarCarrito'),
    path('listarCategoria', views.listarCategoria, name='listarCategoria'),
    path('anadirProducto', views.anadirProducto, name='anadirProducto'),
    path('anadirCategoria', views.anadirCategoria, name='anadirCategoria'),
    path('buscarCategoria/<int:pk>', views.buscarCategoria, name='buscarCategoria'),
    path('anadirProductoForm', views.anadirProductoForm, name='anadirProductoForm'),
]