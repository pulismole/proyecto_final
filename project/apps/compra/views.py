from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models


class ClienteCreate(CreateView):
    model = models.Cliente
    form_class = forms.ClienteForm
    success_url = reverse_lazy("compra:index")

class CompraDetail(DetailView):
    model = models.Compra


class CompraList(ListView):
    model = models.Compra

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Compra.objects.filter(nombre__icontains=query)
        else:
            object_list = models.Compra.objects.all()
        return object_list


class CompraCreate(CreateView):
    model = models.Compra
    form_class = forms.CompraForm
    success_url = reverse_lazy("compra:index")

    def form_valid(self, form):
        form.instance.cliente = self.request.user.cliente
        return super().form_valid(form)


class CompraDelete(DeleteView):
    model = models.Compra
    success_url = reverse_lazy("compra:compra_list")


class CompraUpdate(UpdateView):
    model = models.Compra
    success_url = reverse_lazy("compra:compra_list")
    form_class = forms.CompraForm