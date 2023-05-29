from django import forms

from . import models

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = "__all__"

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.ProductoCategoria
        fields = "__all__"

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"
