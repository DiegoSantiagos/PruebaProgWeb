from django.db import models
from django.conf import settings

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre + ' ' + self.descripcion

class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=10)
    imagen = models.FileField(upload_to='imagenesProductos/', null=True)
    stock = models.IntegerField(default=0)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre + ' ' + self.precio + ' ' + self.descripcion 
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    foto = models.FileField(upload_to='fotoUsuario/', null=True)
    contrasena = models.CharField(max_length=50)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido + ' ' + self.email + ' ' + self.contrasena

class Carrito(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.producto.nombre + ' ' + str(self.fecha_agregado) + ' ' + str(self.cantidad)

class Direccion(models.Model):
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50, null=True)
    pais = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.direccion + ' ' + self.ciudad + ' ' + self.estado + ' ' + self.pais + ' ' + self.codigo_postal
    
class MetodoPago(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    numero = models.CharField(max_length=20)
    mesExpiracion = models.CharField(max_length=2)
    anioExpiracion = models.CharField(max_length=2)
    cvv = models.CharField(max_length=3)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre + ' ' + self.numero + ' ' + str(self.fecha_expiracion) + ' ' + self.cvv + ' ' + str(self.fecha_modificacion)

class Comentarios(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.producto.nombre + ' ' + self.comentario + ' ' + str(self.fecha_creacion) + ' ' + str(self.fecha_modificacion)

class Compras(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.producto.nombre + ' ' + str(self.fecha_compra) + ' ' + str(self.cantidad) + ' ' + str(self.total)
    
class registroCompras(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario + ' ' + self.producto.nombre + ' ' + str(self.cantidad) + ' ' + str(self.total) + ' ' + str(self.fecha_compra) + ' ' + self.direccion + ' ' + self.metodo_pago    

class favoritos(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario + ' ' + self.producto.nombre