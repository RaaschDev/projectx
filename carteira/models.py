from django.db import models
from django.contrib.auth.models import User

from bebidas.models import BebidaModel
from comidas.models import ComidaModel
from ingresso_venda.models import IngressoVenda


class Carteira(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    ingressos = models.ManyToManyField(IngressoVenda)
    bebidas = models.ManyToManyField(BebidaModel)
    comidas = models.ManyToManyField(ComidaModel)

    def __str__(self):
        return f'{self.user}'
