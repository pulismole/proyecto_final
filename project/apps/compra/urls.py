from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="compra/index.html"), name="index"),
    path("compra/list/", views.CompraList.as_view(), name="compra_list"),
    path("compra/detail/<int:pk>", views.CompraDetail.as_view(), name="compra_detail"),
    path("compra/create/", staff_member_required(views.CompraCreate.as_view()), name="compra_create"),
    path("compra/delete/<int:pk>", staff_member_required(views.CompraDelete.as_view()), name="compra_delete"),
    path("compra/update/<int:pk>", staff_member_required(views.CompraUpdate.as_view()), name="compra_update"),
]