from django.db import models
from django.utils import timezone

class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Categoría de Productos"
        verbose_name_plural = "Categorías de Productos"

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True)
    categoria = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, null=True)
    fecha_vencimiento = models.DateField(null=True)
    fecha_actualizacion = models.DateTimeField(default=timezone.now, editable=False, verbose_name="fecha de actualización")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre