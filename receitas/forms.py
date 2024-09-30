from django import forms
from django.forms import ModelForm
from .models import *

class RecipeForm(forms.ModelForm):
    class Meta:

        model = Receita
        fields = '__all__'