# myapp/views.py
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Categoria, Cliente, Producto, Compra
from .forms import CategoriaForm, ClienteForm, ProductoForm, CompraForm

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categorias.html'

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'nuevo-registro.html'

class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes.html'

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'nuevo-registro.html'

class ProductoListView(ListView):
    model = Producto
    template_name = 'productos.html'

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'nuevo-registro.html'

class CompraListView(ListView):
    model = Compra
    template_name = 'compras.html'

class CompraCreateView(CreateView):
    model = Compra
    form_class = CompraForm
    template_name = 'nueva-compra.html'