from django import forms
from .models import Animal, Habitat, Cuidador

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nombre', 'edad', 'especie', 'descripcion']

class HabitatForm(forms.ModelForm):
    class Meta:
        model = Habitat
        fields = ['nombre', 'ubicacion', 'descripcion']

class CuidadorForm(forms.ModelForm):
    class Meta:
        model = Cuidador
        fields = ['nombre', 'edad', 'telefono']

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)
