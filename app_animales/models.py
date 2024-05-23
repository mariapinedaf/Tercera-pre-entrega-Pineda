from django.db import models

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    especie = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Habitat(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Cuidador(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

