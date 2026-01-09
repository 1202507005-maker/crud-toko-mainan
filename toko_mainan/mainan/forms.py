from django import forms
from .models import Mainan

class MainanForm(forms.ModelForm):
    class Meta:
        model = Mainan
        fields = '__all__'