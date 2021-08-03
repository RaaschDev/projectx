from django.urls import path
from .views import CreateEvent

urlpatterns = [
    path('', CreateEvent.as_view(), name='add_evento'),
]
