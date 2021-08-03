from django.forms import ModelForm
from .models import EventoModel


class EventoForm(ModelForm):
    model = EventoModel
    fields = '__all__'
