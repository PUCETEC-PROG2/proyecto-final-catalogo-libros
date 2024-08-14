from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer
from django.shortcuts import get_object_or_404, redirect, render
from pokedex.forms import PokemonForm, TrainerForm

#Importaciones libreria de autenticacion de Django
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

def index(request):
    ##pokemons = Pokemon.objects.all() ##SELEC*FROM pokedex_pokemon
    pokemons = Pokemon.objects.order_by('type')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))


@login_required
def pokemon(request, pokemon_id):
    # SELECT *FROM pokedex_pokemon Where id= 'Pokemon_id'
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
    
    return render(request, 'pokemon_form.html',{'form':form})

@login_required
def edit_pokemon(request, id):
    pokemon = get_object_or_404(Pokemon, pk = id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm(instance=pokemon)
    
    return render(request, 'pokemon_form.html',{'form':form})

@login_required
def delete_pokemon(request, id):
    pokemon = get_object_or_404(Pokemon, pk = id)
    pokemon.delete()
    return redirect('pokedex:index')

# Vistas para Trainer
def trainers(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainers.html', {'trainers': trainers})

def trainer_detail(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    return render(request, 'trainer_detail.html', {'trainer': trainer})

@login_required
def add_trainer(request):
    if request.method == "POST":
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:trainers')
    else:
        form = TrainerForm()
    return render(request, 'trainer_form.html', {'form': form})

@login_required
def edit_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    if request.method == "POST":
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('pokedex:trainers')
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'trainer_form.html', {'form': form})

@login_required
def delete_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    if request.method == "POST":
        trainer.delete()
        return redirect('pokedex:trainers')
    return render(request, 'delete_trainer.html', {'trainer': trainer})

class CustomLoginView(LoginView):
    template_name = 'login.html'