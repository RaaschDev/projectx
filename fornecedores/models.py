from django.db import models
from eventos.models import EventoModel

class Fornecedor(models.Model):

    STATUS_CHOICES=(
        ('1','Aberto'),
        ('2','Pago'),
        ('3','Atrazo'),
    )


    nome = models.CharField(max_length=155)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=155)
    evento = models.ForeignKey(EventoModel, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    data = models.CharField(max_length=10)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    banco_nome = models.CharField(max_length=155)
    conta = models.IntegerField()
    agencia = models.IntegerField()
    digito = models.IntegerField()
