from django.contrib import admin

from . import models

admin.site.register(models.ProductoCategoria)
admin.site.register(models.Producto)
admin.site.register(models.Cliente)
admin.site.register(models.Compra)