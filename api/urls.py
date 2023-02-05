from django.urls import path
from .views import EntrenadorPokemonView

urlpatterns = [
    path('entrenador/', EntrenadorPokemonView.as_view(), name='entrenador_list'),
]

