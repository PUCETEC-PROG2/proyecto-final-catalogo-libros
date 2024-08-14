# compras/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CompraListView.as_view(), name='compras'),
    path('nueva-compra/', views.CompraCreateView.as_view(), name='nueva-compra'),
]