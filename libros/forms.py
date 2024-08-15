from django import forms
from .models import Author,Catalog,Book,Client,Compra
        
class AuthorForm(forms.ModelForm):
       class Meta:
        model = Author
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CatalogForm(forms.ModelForm):
       class Meta:
        model = Catalog
        fields = '__all__'
        widgets = {
            'status': forms.TextInput(attrs={'class': 'form-control'}),
           # 'genre': forms.TextInput(attrs={'class': 'form-control'}),
            #'customer_status': forms.TextInput(attrs={'class': 'form-control'}),
            #'payment_type': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class CatalogForm(forms.ModelForm):
       class Meta:
        model = Catalog
        fields = '__all__'
        widgets = {    
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class BookForm(forms.ModelForm):
       class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
        }
        
class ClientForm(forms.ModelForm):
       class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'id_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ('cliente', 'fecha', 'productos')
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'productos': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }