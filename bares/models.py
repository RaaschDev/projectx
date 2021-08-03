from django.db import models

from eventos.models import EventoModel
from perfil_empresa.models import PerfilEmpresa


class BarModel(models.Model):
    evento = models.ForeignKey(EventoModel, on_delete=models.CASCADE)
    nome = models.CharField(max_length=155)
    user = models.ManyToManyField(PerfilEmpresa)

    def __str__(self):
        return self.nome
