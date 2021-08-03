from django.contrib.auth.models import User
from django.db import models

from eventos.models import EventoModel


class ArtistaModel(models.Model):
    evento = models.ForeignKey(EventoModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=155)
    spotfy = models.URLField(blank=True, null=True)
    # img = models.ImageField(upload_to='artistas/')

    def __str__(self):
        return self.name


class EventoArtistaModel(models.Model):
    evento = models.ForeignKey(EventoModel, on_delete=models.CASCADE)
    artista = models.ForeignKey(ArtistaModel, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return f'{self.artista}'
