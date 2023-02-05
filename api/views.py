from django.shortcuts import render
from django.views import View
from .models import EntrenadorPokemon
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

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

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        jd = json.loads(request.body)
        print(jd)
        EntrenadorPokemon.objects.create(
            region = jd['region'], 
            tipo = jd['tipo'], 
            numero_medallas = jd['numero_medallas']
            )
        datos={'message':"Entrenador creado!"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        entrenadores = list(EntrenadorPokemon.objects.filter(id=id).values())
        if len(entrenadores)>0:
            entrenador = EntrenadorPokemon.objects.get(id=id)
            entrenador.region = jd['region']
            entrenador.tipo = jd['tipo']
            entrenador.numero_medallas = jd['numero_medallas']
            entrenador.save()
            datos={'message':"Entrenador editado!"}
        else:
            datos={'message':"Entrenador no encontrado..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        Entrenadores = list(EntrenadorPokemon.objects.filter(id=id).values())
        if len(Entrenadores)>0:
            EntrenadorPokemon.objects.filter(id=id).delete()
            datos={'message':"Entrenador eliminado!"}
        else:
            datos={'message':"Entrenador no encontrado..."}
        return JsonResponse(datos)