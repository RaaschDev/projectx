from django.db import models
from empresa.models import EmpresaModel


class EventoModel(models.Model):
    empresa = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE)
    name = models.CharField('Nome', max_length=155)
    tipo = models.CharField(max_length=155)
    date = models.DateField('Data')
    start = models.TimeField('Inicio',)
    end = models.TimeField('Fim', max_length=5)
    endereco = models.CharField('Endereco', max_length=200)
    endereco2 = models.CharField('Endereco 2', max_length=200, blank=True, null=True)
    img = models.ImageField('Imagem', upload_to='eventos/media/')
    advertising = models.ImageField('Propaganda', upload_to='eventos/advertising/')
    aprovado = models.BooleanField(default=False , blank=False, null=False)
    comissao = models.IntegerField(blank=True, null=True)




    def __str__(self):
        return f'{self.name}'
