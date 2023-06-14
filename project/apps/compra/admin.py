from django.contrib import admin

from . import models

admin.site.register(models.Cliente)


@admin.register(models.Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = (
        "cliente",
        "producto",
        "cantidad",
        "precio_total",
        "fecha_venta",
    )
    list_display_links = ("producto",)
    search_fields = ("producto.nombre", "cliente")
    list_filter = ("cliente",)
    date_hierarchy = "fecha_venta"