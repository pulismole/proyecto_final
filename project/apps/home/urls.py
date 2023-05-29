from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('registrar_compra/', views.registrar_compra, name='registrar_compra'),
]