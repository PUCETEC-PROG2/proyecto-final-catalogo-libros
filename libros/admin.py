from django.contrib import admin
from .models import Author,Catalog
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    pass