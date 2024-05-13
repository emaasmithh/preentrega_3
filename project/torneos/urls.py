from django.urls import path

from torneos.views import index, torneos_create, torneos_list

app_name = "torneos"

urlpatterns = [
    path("", index, name="index"),
    path("torneos/list", torneos_list, name="torneos_list"),
    path("torneos/create", torneos_create, name="torneos_create"),
]