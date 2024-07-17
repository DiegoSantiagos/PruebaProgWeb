from django.shortcuts import render, redirect
from .models import Productos,Usuario,Compras,Carrito,Direccion,MetodoPago,Comentarios,Categoria
from .forms import UsuarioForm , ProductoForm, CategoriaForm,CustomUserForm, MetodoPagoForm, DireccionForm
from tienda.settings import MEDIA_URL
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate, login
from django.contrib.auth.models import User
from django.db.models import Sum
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

@login_required
def listarCarrito(request):
    listadoCarrito = Carrito.objects.filter(usuario=request.user)
    context = {'listadoCarrito': listadoCarrito}
    totalPagar = sum(int(item.producto.precio) * item.cantidad for item in listadoCarrito)
    totalProductos = Carrito.objects.filter(usuario=request.user).aggregate(Sum('cantidad'))['cantidad__sum']
    context['totalProductos'] = totalProductos
    context['totalPagar'] = totalPagar
    
    return render(request, 'listarCarrito.html', context)

def listarCategoria(request):
    listadoCategoria = Categoria.objects.all()
    context = {'listado': listadoCategoria}
    return render(request, 'listarCategoria.html', context)

@login_required
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

@login_required
def anadirCarrito(request, pk):
    context = {}
    try:
        if request.method == 'POST':
            if 'btnAnadir' in request.POST:
                usuario = request.user
                producto = Productos.objects.get(pk=pk)
                varCantidad = int(request.POST.get('txtCantidad' + str(pk), 1))
                carrito, creado = Carrito.objects.get_or_create(
                    producto=producto,
                    cantidad= varCantidad,
                    usuario = usuario
                )
                context['exito'] = 'Producto añadido al carrito correctamente'
                
                if not creado:
                    carrito.cantidad += varCantidad
                    carrito.save()
                    context['exito'] = 'Producto sumado al carrito correctamente'
    except Productos.DoesNotExist:
        context['error'] = 'El producto no existe'
    listadoCarrito = Carrito.objects.filter(usuario=request.user)
    context = {'listadoCarrito': listadoCarrito}
    totalPagar = sum(int(item.producto.precio) * item.cantidad for item in listadoCarrito)
    totalProductos = Carrito.objects.filter(usuario=request.user).aggregate(Sum('cantidad'))['cantidad__sum']
    context['totalProductos'] = totalProductos
    context['totalPagar'] = totalPagar
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
    listadoCarrito = Carrito.objects.filter(usuario=request.user)
    context = {'listadoCarrito': listadoCarrito}
    totalPagar = sum(int(item.producto.precio) * item.cantidad for item in listadoCarrito)
    totalProductos = Carrito.objects.filter(usuario=request.user).aggregate(Sum('cantidad'))['cantidad__sum']
    context['totalProductos'] = totalProductos
    context['totalPagar'] = totalPagar
    return render(request, 'listarCarrito.html', context)

@login_required
def actualizarCarrito(request, pk):
    context = {}
    if request.method == 'POST':
        try:
            carrito = Carrito.objects.get(pk=pk)
            cantidadFinal = int(request.POST.get('txtCantidad' + str(pk), 1))
            if cantidadFinal < 1:
                context['error'] = 'La cantidad no puede ser menor a 1'
            elif cantidadFinal > carrito.producto.stock:
                context['error'] = 'La cantidad no puede ser mayor al stock'
            else:
                carrito.cantidad = cantidadFinal
                carrito.save()
                context['exito'] = 'Carrito actualizado correctamente'
        except:
            context['error'] = 'Error al actualizar el carrito'
    listadoCarrito = Carrito.objects.filter(usuario=request.user)
    totalPagar = sum(int(item.producto.precio) * item.cantidad for item in listadoCarrito)
    totalProductos = Carrito.objects.filter(usuario=request.user).aggregate(Sum('cantidad'))['cantidad__sum']
    # context = {'listadoCarrito': listadoCarrito}
    # context['totalProductos'] = totalProductos
    # context['totalPagar'] = totalPagar
    context.update({
        'listadoCarrito': listadoCarrito,
        'totalProductos': totalProductos,
        'totalPagar': totalPagar
    })
    return render(request, 'listarCarrito.html', context)

@login_required
def anadirTarjetaForm(request):
    context = {'form': MetodoPagoForm()}
    if request.method == 'POST':
        if 'btnGuardar' in request.POST:
            item = None
            if request.POST['txtId'] != '0':
                item = MetodoPago.objects.get(pk=request.POST['txtId'])
            form = MetodoPagoForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                context['exito'] = 'Tarjeta añadida correctamente'
            else:
                context['error'] = 'Error al guardar la tarjeta'
            context['listadoTarjeta'] = MetodoPago.objects.all()
        else:
            context['listadoTarjeta'] = MetodoPago.objects.all()
    context['meses'] = range(1, 13)
    context['anios'] = range(24, 41)
    return render(request, 'anadirTarjetaForm.html', context)

@login_required
def editarTarjeta(request, pk):
    context = {}
    try:
        item = MetodoPago.objects.get(pk=pk)
        context['item'] = item
        context['form'] = MetodoPagoForm(instance=item)
    except:
        context['error'] = 'Error al buscar el registro'
    return render(request, 'anadirTarjetaForm.html', context)

@login_required
def eliminarTarjeta(request, pk):
    context = {}
    try:
        tarjeta = MetodoPago.objects.get(pk=pk)
        tarjeta.delete()
        context['exito'] = 'Tarjeta eliminada correctamente'
        context['listado'] = MetodoPago.objects.all()
    except:
        context['error'] = 'Error al eliminar la tarjeta'
    context['listado'] = MetodoPago.objects.all()
    return render(request, 'anadirTarjetaForm.html', context)

@login_required
def realizarCompra(request):
    context = {'formPago': MetodoPagoForm() , 'formDireccion': DireccionForm()} 
    
    if request.method == 'POST':
        try:
            direccion = DireccionForm(request.POST)
            pago = MetodoPagoForm(request.POST)
            if direccion.is_valid() and pago.is_valid():
                direccion = direccion.save()
                pago = pago.save()
                totalPagar = sum(int(item.producto.precio) * item.cantidad for item in Carrito.objects.filter(usuario=request.user))
                compra = Compras(usuario=request.user, total=totalPagar, direccion=direccion, metodoPago=pago)
                compra.save()
                for item in Carrito.objects.filter(usuario=request.user):
                    registro = registroCompras(usuario=request.user, producto=item.producto, cantidad=item.cantidad, total=(item.producto.precio * item.cantidad))
                    registro.save()
                    item.delete()
                context['exito'] = 'Compra realizada correctamente'
        except:
            context['error'] = 'Error al realizar la compra'
    context['listadoDireccion'] = Direccion.objects.all()
    context['listadoTarjeta'] = MetodoPago.objects.all()
    context['listadoCarrito'] = Carrito.objects.filter(usuario=request.user)
    return render(request, 'realizarCompra.html', context)  

@login_required
def anadirDireccionForm(request):
    context = {'form': DireccionForm()}
    if request.method == 'POST':
        if 'btnGuardar' in request.POST:
            item = None
            if request.POST['txtId'] != '0':
                item = Direccion.objects.get(pk=request.POST['txtId'])
            form = DireccionForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                context['exito'] = 'Direccion añadida correctamente'
            else:
                context['error'] = 'Error al guardar la direccion'
            context['listadoDireccion'] = Direccion.objects.all()
        else:
            context['listadoDireccion'] = Direccion.objects.all()
    return render(request, 'anadirDireccionForm.html', context)

@login_required
def editarDireccion(request, pk):
    context = {}
    try:
        item = Direccion.objects.get(pk=pk)
        context['item'] = item
        context['form'] = DireccionForm(instance=item)
    except:
        context['error'] = 'Error al buscar el registro'
    return render(request, 'anadirDireccionForm.html', context)

@login_required
def eliminarDireccion(request, pk):
    context = {}
    try:
        direccion = Direccion.objects.get(pk=pk)
        direccion.delete()
        context['exito'] = 'Direccion eliminada correctamente'
        context['listado'] = Direccion.objects.all()
    except:
        context['error'] = 'Error al eliminar la direccion'
    context['listado'] = Direccion.objects.all()
    return render(request, 'anadirDireccionForm.html', context)
    