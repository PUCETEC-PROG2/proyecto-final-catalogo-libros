# productos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductoListView.as_view(), name='productos'),
    path('nuevo-registro/', views.ProductoCreateView.as_view(), name='nuevo-registro'),
]