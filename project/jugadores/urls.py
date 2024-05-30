from django.urls import path

from jugadores.views import index, jugadores_list, jugadores_create, jugadores_detail, jugadores_delete, jugadores_update

app_name = "jugadores"

urlpatterns = [
    path("", index, name="index"),
    path("jugadores/list", jugadores_list, name="jugadores_list"),
    path("jugadores/create", jugadores_create, name="jugadores_create"),
    path("jugadores/detail/<int:pk>", jugadores_detail, name="jugadores_detail"),
    path("jugadores/delete/<int:pk>", jugadores_delete, name="jugadores_delete"),
    path("jugadores/update/<int:pk>", jugadores_update, name="jugadores_update"),
]   