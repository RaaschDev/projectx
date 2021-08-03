from django.db import models


class EmpresaModel(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name
