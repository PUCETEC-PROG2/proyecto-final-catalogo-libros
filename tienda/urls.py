# myapp/urls.py
from django.urls import include, path

urlpatterns = [
    path('categorias/', include('categorias.urls')),
    path('clientes/', include('clientes.urls')),
    path('compras/', include('compras.urls')),
    path('productos/', include('productos.urls')),
]