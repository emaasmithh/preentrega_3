from django import forms

from . import models


class JugadorForm(forms.ModelForm):
    class Meta:
        model = models.Jugador
        fields = ["nombre", "apellido", "posicion", "fecha_nacimiento", "ranking"]