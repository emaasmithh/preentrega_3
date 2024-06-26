from typing import Any
from django.db import models
from django.contrib.auth.models import User

class Jugador(models.Model):
    nombre = models.CharField(max_length=50, unique=False)
    apellido = models.CharField(max_length=50, unique=False)
    posicion = models.CharField(max_length=50, unique=False)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    ranking = models.IntegerField(null=True, blank=True)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="jugador", blank=True, null=True)   

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
    class Meta:
        verbose_name = "jugador"
        verbose_name_plural = "jugadores"