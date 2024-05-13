from django.db import models

class Torneo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "torneo"
        verbose_name_plural = "torneos"