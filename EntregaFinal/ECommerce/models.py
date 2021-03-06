from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    idUser = models.ForeignKey(User, default=0 ,on_delete = models.CASCADE)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField()
    dni = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - E-Mail {self.email}"

class Vendedor(models.Model):
    idUser = models.ForeignKey(User, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    dni = models.IntegerField()
    cuil = models.IntegerField()
    salario = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - E-Mail {self.email}"



class Compra(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete = models.PROTECT)
    idVendedor = models.ForeignKey(Vendedor, on_delete = models.PROTECT)
    direccion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=150)
    codigoPostal = models.IntegerField()
    estado = models.CharField(max_length=150)
    medioPago = models.CharField(max_length=200)
    fechaCompra = models.DateField()
    fechaEnvio = models.DateField()
    fecha = models.DateField()
    comprobantePago = models.IntegerField()

    def __str__(self):
        return f"Compra de: {self.idCliente} - Fecha de Compra: {self.fechaCompra}"

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    categoria = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=5000)
    imagen = models.ImageField()
    stock = models.IntegerField()
    precio = models.IntegerField()

class CompraXProducto(models.Model):
    idCompra = models.ForeignKey(Compra, on_delete= models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete= models.CASCADE)
    cantidad = models.IntegerField()
    precioTotal = models.IntegerField()

class Novedad(models.Model):
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=150)
    contenido = models.CharField(max_length=5000)
    imagen = models.ImageField()
    fecha = models.DateField()

    def __str__(self):
        return f"Titulo: {self.titulo} - subtitulo: {self.subtitulo} - Fecha {self.fecha}"


class Mensaje(models.Model):
    idNovedad = models.ForeignKey(Novedad, on_delete = models.CASCADE)
    idUser = models.ForeignKey(User, on_delete = models.CASCADE)
    mensaje = models.CharField(max_length=5000)
    fecha = models.DateField()

    def __str__(self):
        return f"idNovedad: {self.idNovedad} - idUser: {self.idUser} - fecha {self.fecha}"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to="avatares", null=True, blank = True)