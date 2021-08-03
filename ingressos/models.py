from django.contrib.auth.models import User
from django.db import models

from eventos.models import EventoModel


class IngressoModel(models.Model):
    evento = models.ForeignKey(EventoModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=155)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    lote = models.SmallIntegerField()
    quantidade = models.IntegerField()

    def __str__(self):
        return self.name