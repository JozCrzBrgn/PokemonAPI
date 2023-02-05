from django.shortcuts import render
from django.views import View
from .models import EntrenadorPokemon
from django.http.response import JsonResponse

# Create your views here.
class EntrenadorPokemonView(View):
    def get(self, request, id=0):
        if id>0:
            entrenadores = list(EntrenadorPokemon.objects.filter(id=id).values())
            if len(entrenadores)>0:
                entrenador=entrenadores[0]
                datos={'message':"Entrenador encontrado", 'entrenador':entrenador}
            else:
                datos={'message':"Entrenador no encontrado..."}
            return JsonResponse(datos)
        else:
            entrenadores = list(EntrenadorPokemon.objects.values())
            if len(entrenadores)>0:
                datos={'message':"Entrenador encontrado", 'entrenadores':entrenadores}
            else:
                datos={'message':"Entrenador no encontrado..."}
            return JsonResponse(datos)