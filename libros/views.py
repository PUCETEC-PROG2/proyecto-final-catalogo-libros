from django.http import HttpResponse
from django.template import loader
from .models import Author,Catalog,Book,Client,Compra
from django.shortcuts import get_object_or_404, redirect, render
from libros.forms import AuthorForm,CatalogForm,BookForm,ClientForm,CompraForm
from django.http import JsonResponse

#Importaciones libreria de autenticacion de Django
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

def index(request):
    ##pokemons = Pokemon.objects.all() ##SELEC*FROM libros_pokemon
    books = Book.objects.order_by('title')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'books': books}, request))

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
            return redirect('libros:authors')
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
            return redirect('libros:authors')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author_form.html', {'form': form})

@login_required
def delete_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == "POST":
        author.delete()
        return redirect('libros:authors')
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
            return redirect('libros:catalogs')
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
            return redirect('libros:catalogs')
    else:
        form = AuthorForm(instance=catalog)
    return render(request, 'catalog_form.html', {'form': form})

@login_required
def delete_catalog(request, catalog_id):
    catalog = get_object_or_404(Catalog, id=catalog_id)
    if request.method == "POST":
        catalog.delete()
        return redirect('libros:catalogs')
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
            return redirect('libros:books')
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
            return redirect('libros:books')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form})

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('libros:books')
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
            return redirect('libros:clients')
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
            return redirect('libros:clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {'form': form})

@login_required
def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == "POST":
        client.delete()
        return redirect('libros:clients')
    return render(request, 'delete_client.html', {'client': client})

#Vista para compra

def compras(request):
    compras = Compra.objects.all()
    return render(request, 'detalle_compra.html', {'compras': compras})

def crear_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            compra.save()  # Guarda la instancia de Compra primero para que tenga un ID
            form.save_m2m()  # Guarda las relaciones de muchos a muchos
            compra.total = calcular_total(compra.productos.all())
            compra.save()  # Guarda la instancia de Compra con el total actualizado
            return redirect('libros:detalle_compra', pk=compra.pk)
    else:
        form = CompraForm()
    return render(request, 'crear_compra.html', {'form': form})


def detalle_compra(request, pk):
    compra = Compra.objects.get(pk=pk)
    return render(request, 'detalle_compra.html', {'compra': compra})

def calcular_total(productos):
    total = 0
    for producto in productos:
        total += producto.price
    return total

class CustomLoginView(LoginView):
    template_name = 'login.html'