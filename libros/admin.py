from django.contrib import admin
from .models import Pokemon, Trainer,Author,Catalog
# Register your models here.

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    pass