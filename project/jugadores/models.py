from typing import Any
from django.db import models

class Jugador(models.Model):
    nombre = models.CharField(max_length=50, unique=False)
    apellido = models.CharField(max_length=50, unique=False)
    posicion = models.CharField(max_length=50, unique=False)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
    class Meta:
        verbose_name = "jugador"
        verbose_name_plural = "jugadores"