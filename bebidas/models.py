from django.db import models

from eventos.models import EventoModel


class BebidaModel(models.Model):
    evento = models.ForeignKey(EventoModel, on_delete=models.CASCADE)
    marca = models.CharField(max_length=155)
    quantidade = models.IntegerField()
    custo = models.DecimalField(max_digits=8, decimal_places=2)
    venda = models.DecimalField(max_digits=8, decimal_places=2)
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return self.marca
