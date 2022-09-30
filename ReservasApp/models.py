from http import client
from django.db import models

# Create your models here.
class Cliente(models.Model):
    Nombre = models.CharField(max_length = 50)
    ApePaterno = models.CharField(max_length = 25)
    ApeMaterno = models.CharField(max_length = 25)
    Edad = models.IntegerField()
    Email = models.EmailField(max_length = 255)
    Direccion = models.TextField()

class Habitacion(models.Model):
    Piso =  models.IntegerField()
    Numero = models.IntegerField()
    Precio = models.DecimalField(max_digits = 8, decimal_places = 2)
    enUso = models.BooleanField(default = False)

class Empleado(models.Model):
    NomCompleto = models.CharField(max_length = 100)
    Cargo = models.CharField(max_length = 30)

class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente','Pendiente'),
        ('Pagado','Pagado'),
        ('Eliminado','Eliminado')
    ]
    METODO_PAGO_CHOCIES = [
        ('Efectivo','Efectivo'),
        ('Tarjeta','Tarjeta')
    ]
    Habitacion = models.ForeignKey(Habitacion, on_delete = models.CASCADE)
    Cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    Empleado = models.ForeignKey(Empleado, on_delete = models.CASCADE)
    Estado = models.CharField(max_length = 12, choices = ESTADO_CHOICES)
    DiasEstadia = models.IntegerField()
    FechaIngreso = models.DateTimeField()
    FechaSalida = models.DateTimeField()
    Monto = models.DecimalField(max_digits = 8, decimal_places = 2)
    MetodoPago = models.CharField(max_length =10, choices = METODO_PAGO_CHOCIES)

class Servicio(models.Model):
    Descripcion = models.TextField()
    Precio  = models.DecimalField(max_digits = 8, decimal_places = 2)

class Gastos(models.Model):
    Reserva = models.ForeignKey(Reserva, on_delete = models.CASCADE)
    Servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE)
    cantidad = models.IntegerField()
    TotalGasto = models.DecimalField(max_digits = 8, decimal_places = 2)
