from django.urls import path
from .views import EntrenadorPokemonView, PokemonView

urlpatterns = [
    path('entrenadores/', EntrenadorPokemonView.as_view(), name='entrenadores_list'),
    path('entrenadores/<int:id>', EntrenadorPokemonView.as_view(), name='entrenadores_procesos'),
    path('pokemon/<str:pokemon>', PokemonView.as_view(), name='pokemon'),
]

