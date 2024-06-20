from django.shortcuts import render
from .models import Productos,Usuario,Compras,Carrito,Direccion,MetodoPago,Comentarios,Calificacion,Favoritos,Categoria
# Create your views here.
def menu(request):
    return render(request, 'plantillaBase.html', {})

def index(request):
    context = {}
    return render(request, 'index.html', context)

def listarProductos(request):
    listadoProductos = Productos.objects.all()
    context = {'listadoProductos': listadoProductos}
    return render(request, 'listarProductos.html', context)

def listarCarrito(request):
    listadoCarrito = Carrito.objects.all()
    context = {'listadoCarrito': listadoCarrito}
    return render(request, 'listarCarrito.html', context)

def anadirProducto(request):
    context= {}
    if request.method == 'POST':
        id = request.POST.get('txtId')
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')
        categoria = request.POST.get('categoria')
        if 'btnGuardar' in request.POST:
            if len(nombre.strip()) < 1:
                context['error'] = 'El nombre no puede estar vacío'
            elif len(descripcion.strip()) < 1:
                context['error'] = 'La descripción no puede estar vacía'
            elif len(categoria.strip()) < 1:
                context['error'] = 'La categoria no puede estar vacía'
            else:
                if id == 0:
                    producto = Productos(nombre=nombre,precio=precio,descripcion=descripcion,categoria=categoria)
                else:
                    producto = Productos()
                    producto.id = id
                    producto.nombre = nombre
                    producto.precio = precio
                    producto.descripcion = descripcion
                    producto.categoria = categoria
                producto.save()
                context['exito'] = 'Producto añadido correctamente'
    return render(request, 'anadirProducto.html', context)

def listarCategoria(request):
    listadoCategoria = Categoria.objects.all()
    context = {'listadoCategoria': listadoCategoria}
    return render(request, 'listarCategoria.html', context)

def anadirCategoria(request):
    context = {}
    if request.method == 'POST':
        id = request.POST.get('txtId')
        nombre = request.POST.get('txtNombre')
        descripcion = request.POST.get('txtDescripcion')
        if 'btnGuardar' in request.POST:
            if len(nombre.strip()) < 1:
                context['error'] = 'El nombre no puede estar vacío'
            elif len(descripcion.strip()) < 1:
                context['error'] = 'La descripción no puede estar vacía'
            else:
                if id == 0:
                    categoria = Categoria(nombre=nombre,descripcion=descripcion)
                else:
                    categoria = Categoria()
                    categoria.id =id
                    categoria.nombre = nombre
                    categoria.descripcion = descripcion
        categoria.save()
        context['exito'] = 'Categoria añadida correctamente'
    return render(request, 'anadirCategoria.html', context)