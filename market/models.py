from django.db import models

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
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' ' + self.precio + ' ' + str(self.fecha_creacion) + ' ' + str(self.fecha_modificacion)
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    foto = models.FileField(upload_to='fotoUsuario/', null=True)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    fecha_cuanta = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.nombre + ' ' + self.apellidos + ' ' + self.email + ' ' + str(self.fecha_nacimiento) + ' ' + str(self.fecha_cuanta)

class Compras(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.producto.nombre + ' ' + self.usuario.nombre + ' ' + str(self.fecha_compra) + ' ' + str(self.cantidad) + ' ' + str(self.total)
    
class Carrito(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.producto.nombre + ' ' + self.usuario.nombre + ' ' + str(self.fecha_agregado) + ' ' + str(self.cantidad)
    
class Direccion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    direccion = models.TextField()
    ciudad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.usuario.nombre + ' ' + self.direccion + ' ' + self.ciudad + ' ' + self.estado + ' ' + self.pais + ' ' + self.codigo_postal + ' ' + str(self.fecha_modificacion)
    
class MetodoPago(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    numero = models.CharField(max_length=20)
    fecha_expiracion = models.DateField()
    cvv = models.CharField(max_length=3)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.usuario.nombre + ' ' + self.nombre + ' ' + self.numero + ' ' + str(self.fecha_expiracion) + ' ' + self.cvv + ' ' + str(self.fecha_modificacion)
    
class Comentarios(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.producto.nombre + ' ' + self.usuario.nombre + ' ' + self.comentario + ' ' + str(self.fecha_creacion) + ' ' + str(self.fecha_modificacion)
    
class Calificacion(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    calificacion = models.IntegerField()

    def __str__(self):
        return self.producto.nombre + ' ' + self.usuario.nombre + ' ' + str(self.calificacion)
    
class Favoritos(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.producto.nombre + ' ' + self.usuario.nombre


#* Productos 
#? nombre - precio - imagen - descripcion - fecha_creacion
#* Usuario
#? nombre - apellidos - foto - email - fecha_nacimiento - fecha_cuanta
#* Compras
#? producto - usuario - fecha_compra - cantidad - total
#* Carrito
#? producto - usuario - fecha_agregado - cantidad
#* Direccion
#? usuario - direccion - ciudad - estado - pais - codigo_postal - fecha_modificacion
#* MetodoPago
#? usuario - nombre - numero - fecha_expiracion - cvv - fecha_modificacion
#* Comentarios
#? producto - usuario - comentario - fecha_creacion - fecha_modificacion
#* Calificacion
#? producto - usuario - calificacion
#* Favoritos
#? producto - usuario
#! extension better comments
