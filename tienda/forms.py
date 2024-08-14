# myapp/forms.py
from django import forms
from .models import Categoria, Cliente, Producto, Compra

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre',)

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'apellido', 'categoria')

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'precio', 'categoria')

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ('fecha', 'cliente', 'productos')