from django.shortcuts import render, redirect
from .models import Productos,Usuario,Compras,Carrito,Direccion,MetodoPago,Comentarios,Categoria
from .forms import UsuarioForm , ProductoForm, CategoriaForm,CustomUserForm
from tienda.settings import MEDIA_URL
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate, login
from django.contrib.auth.models import User
# Create your views here.

def registro_usuario(request): 
    contexto = {}
    data = {
        'form':CustomUserForm()
    } 
    if request.method == 'POST':
        formulario = CustomUserForm(data=request.POST )
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to= 'index')
        data ["form"] = formulario
    return render (request, 'registrar.html' , data )


def menu(request):
    return render(request, 'plantillaBase.html', {})

def index(request):  #obtiene los productos de la base
    productos = Productos.objects.filter(stock__gt=0).order_by('?')[:3]
    context = {'productos': productos}
    context['MEDIA_URL'] = MEDIA_URL
    return render(request, 'index.html', context)

def listarProductos(request):
    listadoProductos = Productos.objects.all()
    context = {'listadoProductos': listadoProductos}
    context['MEDIA_URL'] = MEDIA_URL
    return render(request, 'listarProductos.html', context)

def listarCarrito(request):
    listadoCarrito = Carrito.objects.filter(usuario=request.user)
    context = {'listadoCarrito': listadoCarrito}
    return render(request, 'listarCarrito.html', context)

def listarCategoria(request):
    listadoCategoria = Categoria.objects.all()
    context = {'listado': listadoCategoria}
    return render(request, 'listarCategoria.html', context)

@login_required
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

@login_required
def anadirCategoriaForm(request):
    context = {'form': CategoriaForm()}
    if request.method == 'POST':
        if 'btnGuardar' in request.POST:
            item = None
            if request.POST['txtId'] != '0':
                item = Categoria.objects.get(pk=request.POST['txtId'])
            form = CategoriaForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                context['exito'] = 'Categoria añadida correctamente'
            else:
                context['error'] = 'Error al guardar la categoria'
            context['listado'] = Categoria.objects.all()
        else:
            context['listado'] = Categoria.objects.all()
    return render(request, 'anadirCategoriaForm.html', context)

@login_required
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
        if request.method == 'POST':
            if 'btnAnadir' in request.POST:
                usuario = request.user
                producto = Productos.objects.get(pk=pk)
                varCantidad = 'txtCantidad' + str(pk)
                cantidad = int(request.POST.get(varCantidad, 1))
                
                carrito, creado = Carrito.objects.get_or_create(
                    producto=producto,
                    defaults={'cantidad': cantidad},
                    usuario = usuario
                )
                context['exito'] = 'Producto añadido al carrito correctamente'
                
                if not creado:
                    carrito.cantidad += cantidad
                    carrito.save()
                    context['exito'] = 'Producto sumado al carrito correctamente'
    except Productos.DoesNotExist:
        context['error'] = 'El producto no existe'
        
    context = {'listadoCarrito': Carrito.objects.filter(usuario=request.user)}
    return render(request, 'listarCarrito.html', context)

def verProducto(request, pk):
    context = {}
    try:
        item = Productos.objects.get(pk=pk)
        context['item'] = item
        randProductos = Productos.objects.order_by('?')[:4]
        context['randProductos'] = randProductos
    except Productos.DoesNotExist:
        context['error'] = 'El producto no existe'
    
    
    
    context['MEDIA_URL'] = MEDIA_URL
    return render(request, 'verProducto.html', context)

@login_required
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
def eliminarProducto(request, pk):
    context = {}
    try:
        producto = Productos.objects.get(pk=pk)
        producto.delete()
        context['exito'] = 'Producto eliminado correctamente'
        context['listadoProductos'] = Productos.objects.all()
        
    except:
        context['error'] = 'Error al eliminar el producto'
    context['listadoProductos'] = Productos.objects.all()
    context['MEDIA_URL'] = MEDIA_URL
    return render(request, 'listarProductos.html', context)

@login_required
def eliminarCategoria(request, pk):
    context = {}
    try:
        categoria = Categoria.objects.get(pk=pk)
        categoria.delete()
        context['exito'] = 'Categoria eliminada correctamente'
        context['listado'] = Categoria.objects.all()
    except:
        context['error'] = 'Error al eliminar la categoria'
    context['listado'] = Categoria.objects.all()
    return render(request, 'listarCategoria.html', context)

@login_required
def editarCategoria(request, pk):
    context = {}
    try:
        item = Categoria.objects.get(pk=pk)
        context['item'] = item
        context['form'] = CategoriaForm(instance=item)
    except:
        context['error'] = 'Error al buscar el registro'
    return render(request, 'anadirCategoriaForm.html', context)

@login_required
def eliminarCarrito(request, pk):
    context = {}
    try:
        carrito = Carrito.objects.get(pk=pk)
        carrito.delete()
        context['exito'] = 'Carrito eliminado correctamente'
        context['listadoCarrito'] = Carrito.objects.all()
    except:
        context['error'] = 'Error al eliminar el carrito'
    context['listadoCarrito'] = Carrito.objects.filter(usuario=request.user)
    return render(request, 'listarCarrito.html', context)
