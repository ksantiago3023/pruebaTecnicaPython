from curses.ascii import NUL
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

class Clientes(models.Model):
    GLN = models.CharField(max_length=20,primary_key=True)
    nombre = models.CharField(max_length=50)

class Sucursal(models.Model):
    GLN = models.CharField(max_length=20,primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50,default='')

class Producto(models.Model):
    Gtin = models.CharField(max_length=20,primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

class Pendientes(models.Model):
    id = models.BigAutoField(primary_key=True)
    key_s3 = models.CharField(max_length=100)  # key en s3 para leer y procesar
    procesado = models.BooleanField(default=False,null=True)  # bandera de si ya se enviaron los datos a la tabla del Inventario

# Create your models here.
class Inventario(models.Model):
    FechaInventario = models.CharField(max_length=20)
    GLN_Cliente = models.ForeignKey(Clientes,on_delete=models.CASCADE)
    GLN_Sucrusal = models.ForeignKey(Sucursal,on_delete=models.CASCADE)
    Gtin_Producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    Inventario_Final = models.IntegerField(default=0)
    PrecioUnidad = models.FloatField(default=0)
    consecutivo = models.ForeignKey(Pendientes,on_delete=models.CASCADE,default=0)

