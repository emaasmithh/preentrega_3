from django.urls import path

from jugadores.views import index, jugadores_list, jugadores_create

app_name = "jugadores"

urlpatterns = [
    path("", index, name="index"),
    path("jugadores/list", jugadores_list, name="jugadores_list"),
    path("jugadores/create", jugadores_create, name="jugadores_create"),
]   