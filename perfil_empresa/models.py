from django.contrib.auth.models import User
from django.db import models

from empresa.models import EmpresaModel


class PerfilEmpresa(models.Model):
    empresa = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gestor = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user}'
