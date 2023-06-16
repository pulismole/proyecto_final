from django.contrib import admin

from . import models

admin.site.site_title = "Productos"
admin.site.site_header = "LISTA DE PRODUCTOS"


@admin.register(models.ProductoCategoria)
class ProductoCategoriaAdmin(admin.ModelAdmin):
    """
    - list_display: tupla que especifica los campos que se mostrarán en la lista de objetos
    - search_fields: tupla que especifica los campos por los que se puede buscar en la lista de objetos
    - list_filter: tupla que especifica los campos por los que se puede filtrar en la lista de objetos
    - ordering: tupla que especifica el orden en que se mostrarán los objetos
    """

    list_display = ("nombre",)
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)


@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "descripcion",
        "categoria",
        "stock",
        "precio",
        "fecha_vencimiento",
    )
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = (
        "nombre",
        "categoria",
    )
    list_filter = ("categoria",)
    date_hierarchy = "fecha_actualizacion"