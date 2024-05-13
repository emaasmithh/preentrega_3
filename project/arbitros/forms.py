from django import forms

from . import models


class ArbitroForm(forms.ModelForm):
    class Meta:
        model = models.Arbitro
        fields = ["nombre", "apellido"]