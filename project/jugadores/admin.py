from django.contrib import admin
from .models import Jugador



class JugadorAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "apellido",
        "posicion",
        "fecha_nacimiento",
        "ranking",
    )
    list_display_links = ("nombre",)
    list_filter = ("ranking",)

admin.site.register(Jugador, JugadorAdmin)
