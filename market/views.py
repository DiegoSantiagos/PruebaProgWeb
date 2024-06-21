from django.shortcuts import render
from .models import Productos,Usuario,Compras,Carrito,Direccion,MetodoPago,Comentarios,Calificacion,Favoritos,Categoria
from .forms import UsuarioForm , ProductoForm
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
    context['Categoria'] = Categoria.objects.all()
    
    if request.method == 'POST':
        id = request.POST['txtId']
        nombre = request.POST['txtNombre']
        precio = request.POST['txtPrecio']
        descripcion = request.POST['txtDescripcion']
        idCategoria = request.POST['cmbCategoria']
        
        if 'btnGuardar' in request.POST:
            if len(nombre.strip()) < 1:
                context['error'] = 'El nombre no puede estar vacío'
            elif len(descripcion.strip()) < 1:
                context['error'] = 'La descripción no puede estar vacía'
            else:
                categoria = Categoria.objects.get(pk = idCategoria)
                if id == "0":
                    Productos.objects.create(nombre=nombre,precio=precio,descripcion=descripcion,Categoria=categoria)
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

def buscarCategoria(request, pk):
    context = {}
    try:
        item = Categoria.objects.get(pk = pk)
        context['item'] = item
    except:
        context['error'] = 'Error al buscar el registro'

    return render(request, 'guardarEscuela.html', context)

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