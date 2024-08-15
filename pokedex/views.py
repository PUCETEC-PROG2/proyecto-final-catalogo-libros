from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer, Author,Catalog,Book,Client
from django.shortcuts import get_object_or_404, redirect, render
from pokedex.forms import PokemonForm, TrainerForm,AuthorForm,CatalogForm,BookForm,ClientForm

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

# Vistas para Author

def authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'author_detail.html', {'author': author})

@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:authors')
    else:
        form = AuthorForm()
    return render(request, 'author_form.html', {'form': form})

@login_required
def edit_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect('pokedex:authors')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author_form.html', {'form': form})

@login_required
def delete_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == "POST":
        author.delete()
        return redirect('pokedex:authors')
    return render(request, 'delete_author.html', {'author': author})


# Vistas para Catalogo

def catalogs(request):
    catalogs = Catalog.objects.all()
    return render(request, 'catalogs.html', {'catalogs': catalogs})

def catalog_detail(request, catalog_id):
    catalog = get_object_or_404(Catalog, id=catalog_id)
    return render(request, 'catalog_detail.html', {'catalog': catalog})

@login_required
def add_catalog(request):
    if request.method == "POST":
        form = CatalogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:catalogs')
    else:
        form = CatalogForm()
    return render(request, 'catalog_form.html', {'form': form})

@login_required
def edit_catalog(request, catalog_id):
    catalog = get_object_or_404(Catalog, id=catalog_id)
    if request.method == "POST":
        form = CatalogForm(request.POST, request.FILES, instance=catalog)
        if form.is_valid():
            form.save()
            return redirect('pokedex:catalogs')
    else:
        form = AuthorForm(instance=catalog)
    return render(request, 'catalog_form.html', {'form': form})

@login_required
def delete_catalog(request, catalog_id):
    catalog = get_object_or_404(Catalog, id=catalog_id)
    if request.method == "POST":
        catalog.delete()
        return redirect('pokedex:catalogs')
    return render(request, 'delete_catalog.html', {'catalog': catalog})


# Vistas para libros

def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

@login_required
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:books')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('pokedex:books')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form})

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('pokedex:books')
    return render(request, 'delete_book.html', {'book': book})

# Vistas para clientes

def clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})

def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'client_detail.html', {'client': client})

@login_required
def add_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:clients')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})

@login_required
def edit_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('pokedex:clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {'form': form})

@login_required
def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == "POST":
        client.delete()
        return redirect('pokedex:clients')
    return render(request, 'delete_client.html', {'client': client})

class CustomLoginView(LoginView):
    template_name = 'login.html'