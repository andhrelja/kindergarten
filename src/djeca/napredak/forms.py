from django import forms
from racuni.forms import DateInput
from .models import DijeteNapredak


class DijeteNapredakForm(forms.ModelForm):
    
    class Meta:
        model = DijeteNapredak
        fields = ("datum_start", "datum_kraj", "ocjena", "komentar", "dijete")
        widgets = {
            'komentar': forms.Textarea(attrs={'class': 'form-control'}),
            'datum_start': DateInput(attrs={'class': 'form-control'}),
            'datum_kraj': DateInput(attrs={'class': 'form-control'}),
            'ocjena': forms.Select(attrs={'class': 'form-control'}),
            'dijete': forms.HiddenInput()
        }
