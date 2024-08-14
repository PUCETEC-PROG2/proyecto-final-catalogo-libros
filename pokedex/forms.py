from django import forms
from .models import Pokemon, Trainer

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