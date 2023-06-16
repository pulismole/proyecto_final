from django import forms

from .models import Cliente, Compra

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ["cliente", "producto", "cantidad"]
        widgets = {
            "cliente": forms.Select(attrs={"class": "form-control"}),
            "producto": forms.Select(attrs={"class": "form-control"}),
            "cantidad": forms.NumberInput(attrs={"class": "form-control"}),
        }