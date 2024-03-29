from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(max_length=60)
    categoria = models.CharField(max_length=60)
    precio_compra = models.FloatField()
    precio_venta = models.FloatField()

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"

class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60) 
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"    

class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    articulo = models.CharField(max_length=60) 
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.articulo}"
    
class Compra(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    distribuidor = models.CharField(max_length=60)
    articulo = models.CharField(max_length=60) 
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.articulo}, {self.distribuidor}" 
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}, {self.imagen}" 