from django.contrib import admin
from .models import Productos,Usuario,Compras,Carrito,Direccion,MetodoPago,Comentarios,Categoria
# Register your models here.

admin.site.register(Productos)
admin.site.register(Usuario)
admin.site.register(Compras)
admin.site.register(Carrito)
admin.site.register(Direccion)
admin.site.register(MetodoPago)
admin.site.register(Comentarios)
admin.site.register(Categoria)

