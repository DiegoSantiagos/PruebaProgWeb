from django.shortcuts import render, redirect
from .models import Productos,Usuario,Compras,Carrito,Direccion,MetodoPago,Comentarios,Calificacion,Favoritos,Categoria
from .forms import UsuarioForm , ProductoForm
from tienda.settings import MEDIA_URL
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


def anadirProducto(request):
    context = {}
    context['Categoria'] = Categoria.objects.all()
    if request.method == 'POST':
        id = int(request.POST.get('txtId', 0))
        nombre = request.POST['txtNombre']
        precio = request.POST['txtPrecio']
        descripcion = request.POST['txtDescripcion']
        idCategoria = request.POST['cmbCategoria']
        imagen = request.FILES.get('txtimagen')
        if 'btnGuardar' in request.POST:
            if len(nombre.strip()) < 1:
                context['error'] = 'El nombre no puede estar vacío'
            elif len(descripcion.strip()) < 1:
                context['error'] = 'La descripción no puede estar vacía'
            else:
                categoria = Categoria.objects.get(pk=idCategoria)
                if id == 0:
                    Productos.objects.create(nombre=nombre, precio=precio, descripcion=descripcion, Categoria=categoria, imagen=imagen)
                else:
                    producto = Productos.objects.get(pk=id)
                    producto.nombre = nombre
                    producto.precio = precio
                    producto.descripcion = descripcion
                    producto.Categoria = categoria 
                    if imagen: 
                        producto.imagen = imagen
                    producto.save()
                context['exito'] = 'Producto añadido correctamente'
    return render(request, 'anadirProducto.html', context)

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

            
        
    # context= {}
    # context['Categoria'] = Categoria.objects.all()
    
    # if request.method == 'POST':
    #     id = request.POST['txtId']
    #     nombre = request.POST['txtNombre']
    #     precio = request.POST['txtPrecio']
    #     descripcion = request.POST['txtDescripcion']
    #     idCategoria = request.POST['cmbCategoria']
        
    #     if 'btnGuardar' in request.POST:
    #         if len(nombre.strip()) < 1:
    #             context['error'] = 'El nombre no puede estar vacío'
    #         elif len(descripcion.strip()) < 1:
    #             context['error'] = 'La descripción no puede estar vacía'
    #         else:
    #             categoria = Categoria.objects.get(pk = idCategoria)
    #             if id == "0":
    #                 Productos.objects.create(nombre=nombre,precio=precio,descripcion=descripcion,Categoria=categoria,foto=foto)
    #             else:
    #                 producto = Productos()
    #                 producto.id = id
    #                 producto.nombre = nombre
    #                 producto.precio = precio
    #                 producto.descripcion = descripcion
    #                 producto.categoria = categoria
    #                 producto.foto = foto
    #                 producto.save()
    #             context['exito'] = 'Producto añadido correctamente'
    # return render(request, 'anadirProducto.html', context)

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