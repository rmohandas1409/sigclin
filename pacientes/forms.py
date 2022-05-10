from django import forms
from .models import *

class ExameForm(forms.ModelForm):

    class Meta:
        model = Exames
        fields = ['codigo', 'exame', 'valor']