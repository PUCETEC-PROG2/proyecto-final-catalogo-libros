# categorias/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoriaListView.as_view(), name='categorias'),
    path('nuevo-registro/', views.CategoriaCreateView.as_view(), name='nuevo-registro'),
]