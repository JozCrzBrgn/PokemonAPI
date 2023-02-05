from django.db import models

# Create your models here.
class EntrenadorPokemon(models.Model):
    region = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    numero_medallas = models.PositiveSmallIntegerField()




