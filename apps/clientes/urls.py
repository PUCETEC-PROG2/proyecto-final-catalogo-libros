# clientes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClienteListView.as_view(), name='clientes'),
    path('nuevo-registro/', views.ClienteCreateView.as_view(), name='nuevo-registro'),
]