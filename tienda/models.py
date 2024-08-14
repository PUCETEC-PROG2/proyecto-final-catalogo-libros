# myapp/models.py
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)

    def __str__(self):
        return f"Compra de {self.cliente} el {self.fecha}"