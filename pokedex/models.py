from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Catalog(models.Model):
    status = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    customer_status = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.status} - {self.genre}'

class Book(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

class BookCatalog(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    added_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('book', 'catalog')

    def __str__(self) -> str:
        return f'{self.book} in {self.catalog}'

class Sale(models.Model):
    date_of_purchase = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_books = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Sale on {self.date_of_purchase} - Total: {self.total}'

class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    catalog = models.ForeignKey(Catalog, on_delete=models.SET_NULL, null=True, blank=True)
    book = models.ManyToManyField(Book, related_name='clients', blank=True)
    sale = models.ManyToManyField(Sale, related_name='clients', blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
