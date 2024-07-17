from django.shortcuts import render, redirect
from .models import Productos,Usuario,Compras,Carrito,Direccion,MetodoPago,Comentarios,Categoria
from .forms import UsuarioForm , ProductoForm, CategoriaForm,CustomUserForm, MetodoPagoForm, DireccionForm
from tienda.settings import MEDIA_URL
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import  authenticate, login
from django.contrib.auth.models import User
from django.db.models import Sum
import logging
logger = logging.getLogger(__name__)

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

def is_superuser(user):
    return user.is_superuser

def menu(request):
    return render(request, 'plantillaBase.html', {})

def index(request): 
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

@login_required
@user_passes_test(is_superuser, login_url='/market/')
def listarCategoria(request):
    listadoCategoria = Categoria.objects.all()
    context = {'listado': listadoCategoria}
    return render(request, 'listarCategoria.html', context)

@login_required
@user_passes_test(is_superuser, login_url='/market/')
def buscarCategoria(request, pk):
    context = {}
    try:
        item = Categoria.objects.get(pk = pk)
        context['item'] = item
    except:
        context['error'] = 'Error al buscar el registro'

    return render(request, 'guardarEscuela.html', context)

@login_required
@user_passes_test(is_superuser, login_url='/market/')
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
@user_passes_test(is_superuser, login_url='/market/')
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
@user_passes_test(is_superuser, login_url='/market/')
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
@user_passes_test(is_superuser, login_url='/market/')
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
@user_passes_test(is_superuser, login_url='/market/')
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
@user_passes_test(is_superuser, login_url='/market/')
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
@user_passes_test(is_superuser, login_url='/market/')
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
                metodoPago = form.save(commit=False)
                metodoPago.usuario = request.user
                form.save()
                context['exito'] = 'Tarjeta añadida correctamente'
            else:
                context['error'] = 'Error al guardar la tarjeta'
            context['listadoTarjeta'] = MetodoPago.objects.filter(usuario=request.user)
        else:
            context['listadoTarjeta'] = MetodoPago.objects.filter(usuario=request.user)
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
    context['listadoDireccion'] = Direccion.objects.filter(usuario=request.user)
    context['listadoTarjeta'] = MetodoPago.objects.filter(usuario=request.user)
    context['listadoCarrito'] = Carrito.objects.filter(usuario=request.user)
    return render(request, 'realizarCompra.html', context)

@login_required
def realizarCompra(request):
    context = {}
    if request.method == 'POST':
        if 'btnComprar' in request.POST:
            try:
                direccion = Direccion.objects.get(pk=request.POST['direccion'])
                tarjeta = MetodoPago.objects.get(pk=request.POST['tarjeta'])
                carrito = Carrito.objects.filter(usuario=request.user)
                totalPagar = sum(int(item.producto.precio) * item.cantidad for item in carrito)
                for item in carrito:
                    compra = Compras(
                        usuario=request.user,  # Asignar el usuario actual
                        producto=item.producto,
                        cantidad=item.cantidad,
                        total=totalPagar,
                        direccion=direccion,
                        metodo_pago=tarjeta
                    )
                    compra.save()
                    item.producto.stock -= item.cantidad
                    item.producto.save()
                    item.delete()
                context['exito'] = 'Compra realizada correctamente'
            except Exception as e:
                logger.error(f"Error al realizar la compra: {e}")
                context['error'] = f"Error al realizar la compra: {e}"
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
                direccion = form.save(commit=False)
                direccion.usuario = request.user
                direccion.save()
                context['exito'] = 'Direccion añadida correctamente'
            else:
                context['error'] = 'Error al guardar la direccion'
        context['listadoDireccion'] = Direccion.objects.filter(usuario=request.user)
    else:
        context['listadoDireccion'] = Direccion.objects.filter(usuario=request.user)
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
    context['listadoDireccion'] = Direccion.objects.all()
    context['listadoTarjeta'] = MetodoPago.objects.all()
    context['listadoCarrito'] = Carrito.objects.filter(usuario=request.user)
    return render(request, 'realizarCompra.html', context)
    