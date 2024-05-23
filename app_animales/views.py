from django.shortcuts import render
from .models import Animal, Habitat, Cuidador
from .forms import AnimalForm, HabitatForm, CuidadorForm, SearchForm

def index(request):
    return render(request, 'app_animales/index.html')

def add_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AnimalForm()
    return render(request, 'app_animales/add_animal.html', {'form': form})

def add_habitat(request):
    if request.method == 'POST':
        form = HabitatForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = HabitatForm()
    return render(request, 'app_animales/add_habitat.html', {'form': form})

def add_cuidador(request):
    if request.method == 'POST':
        form = CuidadorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CuidadorForm()
    return render(request, 'app_animales/add_cuidador.html', {'form': form})

def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Animal.objects.filter(nombre__icontains=query)
            return render(request, 'app_animales/search_results.html', {'results': results, 'query': query})
    else:
        form = SearchForm()
    return render(request, 'app_animales/search.html', {'form': form})

