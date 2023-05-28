from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    desripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    
    def __str__(self):
        return self.nombre