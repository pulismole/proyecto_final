from django import forms

from .models import Compra


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ["producto", "cantidad"]
        widgets = {
            "producto": forms.Select(attrs={"class": "form-control"}),
            "cantidad": forms.NumberInput(attrs={"class": "form-control"}),
        }