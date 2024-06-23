from django.shortcuts import render, redirect
from .models import Productos,Usuario,Compras,Carrito,Direccion,MetodoPago,Comentarios,Calificacion,Favoritos,Categoria
from .forms import UsuarioForm , ProductoForm
from tienda.settings import MEDIA_URL
from django.contrib.auth.decorators import login_required
# Create your views here.
def menu(request):
    return render(request, 'plantillaBase.html', {})

def index(request):
    context = {}
    return render(request, 'index.html', context)

def listarProductos(request):
    listadoProductos = Productos.objects.all()
    context = {'listadoProductos': listadoProductos}
    context['MEDIA_URL'] = MEDIA_URL
    return render(request, 'listarProductos.html', context)

def listarCarrito(request):
    listadoCarrito = Carrito.objects.all()
    context = {'listadoCarrito': listadoCarrito}
    return render(request, 'listarCarrito.html', context)

def listarCategoria(request):
    listadoCategoria = Categoria.objects.all()
    context = {'listadoCategoria': listadoCategoria}
    return render(request, 'listarCategoria.html', context)

def anadirProductoForm(request):
    context = {'form': ProductoForm()}
    if request.method == 'POST':
        if 'btnGuardar' in request.POST:
            item = None
            if request.POST['txtId'] != '0':
                item = Productos.objects.get(pk=request.POST['txtId'])
            form = ProductoForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                form.save()
                context['exito'] = 'Producto añadido correctamente'
            else:
                context['error'] = 'Error al guardar el producto'
            context['listado'] = Productos.objects.all()
            context['MEDIA_URL'] = MEDIA_URL
        else:
            context['listado'] = Productos.objects.all()
            context['MEDIA_URL'] = MEDIA_URL
    else:  # Añade este bloque para manejar las solicitudes GET
        context['listado'] = Productos.objects.all()
        context['MEDIA_URL'] = MEDIA_URL
    return render(request, 'anadirProductoForm.html', context)

def buscarCategoria(request, pk):
    context = {}
    try:
        item = Categoria.objects.get(pk = pk)
        context['item'] = item
    except:
        context['error'] = 'Error al buscar el registro'

    return render(request, 'guardarEscuela.html', context)

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

def editarProducto(request, pk):
    context = {}
    try:
        item = Productos.objects.get(pk=pk)
        context['item'] = item
        context['form'] = ProductoForm(instance=item)
    except:
        context['error'] = 'Error al buscar el registro'
    return render(request, 'anadirProductoForm.html', context)

@login_required
def anadirCarrito(request, pk):
    context = {}
    try:
        producto = Productos.objects.get(pk=pk)
    except Productos.DoesNotExist:
        context['error'] = 'El producto no existe'
    
    carrito, creado = Carrito.objects.get_or_create(
        producto=producto,
        usuario=request.user,
        defaults={'cantidad': 1}
    )
    if not creado:
        carrito.cantidad += 1
        carrito.save()
    
    return render(request, 'listarCarrito.html', context)