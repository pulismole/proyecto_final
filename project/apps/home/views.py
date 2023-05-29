from django.shortcuts import render, redirect

from . import forms

def index(request):
    return render(request, 'home/index.html')

def crear_producto(request):
    if request.method == "POST":
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = forms.ProductoForm()
    return render(request, "home/crear_producto.html", {"form":form})

def crear_categoria(request):
    if request.method == "POST":
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = forms.CategoriaForm()
    return render(request, "home/crear_categoria.html", {"form":form})

def crear_cliente(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = forms.ClienteForm()
    return render(request, "home/crear_cliente.html", {"form":form})