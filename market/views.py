from django.shortcuts import render
from .models import Productos,Usuario,Compras,Carrito,Direccion,MetodoPago,Comentarios,Calificacion,Favoritos
# Create your views here.
def menu(request):
    return render(request, 'plantillaBase.html', {})

def index(request):
    context = {}
    return render(request, 'index.html', context)

def listarProductos(request):
    context = {}
    return render(request, 'listarProductos.html', context)

def listarCarrito(request):
    context = {}
    return render(request, 'listarCarrito.html', context)

def anadirProducto(request ):
    context = {}
    return render(request, 'anadirProducto.html', context)