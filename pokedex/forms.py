from django import forms
from .models import Pokemon, Trainer,Author,Catalog,Book,Client

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
        # labels = {
        #     'name': 'Name',  # Cambiar el texto de la etiqueta
        # }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}), #'style': 'font-weight: bold; color: red;'}
            'type': forms.Select(attrs={'class':'form-control'}),
            'height': forms.NumberInput(attrs={'class':'form-control'}),
            'weight': forms.NumberInput(attrs={'class':'form-control'}),
            'trainer': forms.Select(attrs={'class':'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class':'form-control'})
        }
        
class TrainerForm(forms.ModelForm):
       class Meta:
        model = Trainer
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'level': forms.NumberInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
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
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_status': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_type': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class CatalogForm(forms.ModelForm):
       class Meta:
        model = Catalog
        fields = '__all__'
        widgets = {
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_status': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_type': forms.TextInput(attrs={'class': 'form-control'}),
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