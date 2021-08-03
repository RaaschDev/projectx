from django.contrib import admin
from .models import ArtistaModel, EventoArtistaModel


admin.site.register(ArtistaModel)
admin.site.register(EventoArtistaModel)