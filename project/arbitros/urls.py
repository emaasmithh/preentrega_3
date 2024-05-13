from django.urls import path

from arbitros.views import index, arbitros_list, arbitros_create

app_name = "arbitros"

urlpatterns = [
    path("", index, name="index"),
    path("arbitros/list", arbitros_list, name="arbitros_list"),
    path("arbitros/create", arbitros_create, name="arbitros_create"),
]