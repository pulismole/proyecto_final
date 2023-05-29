from django import forms

from . import models

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.ProductoCategoria
        fields = "__all__"

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = "__all__"

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"

class CompraForm(forms.ModelForm):
    class Meta:
        model = models.Compra
        fields = "__all__"