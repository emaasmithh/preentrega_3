from django.db import models

class Arbitro(models.Model):
    nombre = models.CharField(max_length=50, unique=False)
    apellido = models.CharField(max_length=50, unique=False)
    nacimiento = models.DateField(null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)

    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
    class Meta:
        verbose_name = "arbitro"
        verbose_name_plural = "arbitros"
