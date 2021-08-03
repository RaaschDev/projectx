from django.db import models
from ingressos.models import IngressoModel


class IngressoVenda(models.Model):
    ingresso = models.ForeignKey(IngressoModel, on_delete=models.CASCADE)
    venda_data = models.CharField(max_length=155)
