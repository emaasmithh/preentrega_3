from django import forms

from . import models


class TorneoForm(forms.ModelForm):
    class Meta:
        model = models.Torneo
        fields = ["nombre"]