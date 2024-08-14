# categorias/views.py
from django.shortcuts import render
from django.views import View
from .models import Categoria

class CategoriaListView(View):
    def get(self, request):
        categorias = Categoria.objects.all()
        return render(request, 'categorias.html', {'categorias': categorias})