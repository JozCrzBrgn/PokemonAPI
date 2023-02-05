from django.urls import path
from .views import EntrenadorPokemonView

urlpatterns = [
    path('entrenadores/', EntrenadorPokemonView.as_view(), name='entrenadores_list'),
    path('entrenadores/<int:id>', EntrenadorPokemonView.as_view(), name='entrenadores_procesos'),
]

