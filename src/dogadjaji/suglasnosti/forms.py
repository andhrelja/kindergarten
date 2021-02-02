from django import forms
from .models import Suglasnost

class SuglasnostForm(forms.ModelForm):
    
    class Meta:
        model = Suglasnost
        fields = ("odobren",)
        widgets = {
            "odobren": forms.CheckboxInput(attrs={'class': 'form-control'})
        }
