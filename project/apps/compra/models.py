from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

    def __str__(self):
        return f"{self.nombre}"


class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    producto = models.ForeignKey("producto.Producto", on_delete=models.DO_NOTHING)
    cantidad = models.PositiveIntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    fecha_compra = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ("-fecha_compra",)

    def clean(self):
        if self.cantidad > self.producto.stock:
            raise ValidationError("La cantidad a comprar no puede ser mayor que la cantidad disponible del producto.")

    def save(self, *args, **kwargs):
        self.precio_total = self.producto.precio * self.cantidad
        super().save(*args, **kwargs)
