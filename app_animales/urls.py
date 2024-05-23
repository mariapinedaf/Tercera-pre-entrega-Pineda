from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_animal/', views.add_animal, name='add_animal'),
    path('add_habitat/', views.add_habitat, name='add_habitat'),
    path('add_cuidador/', views.add_cuidador, name='add_cuidador'),
    path('search/', views.search, name='search'),
]
