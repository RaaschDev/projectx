from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import EventoModel
from .forms import EventoForm


class CreateEvent(CreateView):
    model = EventoModel
    fields = '__all__'
    template_name = 'index.html'
