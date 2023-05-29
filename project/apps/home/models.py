from django.db import models

class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True)
    categoria = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, null=True)
    vencimiento = models.DateField(null=True)

    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.producto