from django import forms
from .models import Dijete
from racuni.forms import DateInput

class DijeteForm(forms.ModelForm):
    
    dodatne_informacije = forms.CharField(label="Dodatne informacije", max_length=512, required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Dijete
        fields = ('ime', 'prezime', 'datum_rodjenja', 'dodatne_informacije', 'program')
        widgets = {
            'ime':     forms.TextInput(attrs={'class': 'form-control'}),
            'prezime': forms.TextInput(attrs={'class': 'form-control'}),
            'program': forms.Select(attrs={'class': 'custom-select'}),
            'datum_rodjenja': DateInput(attrs={'class': 'form-control'})
        }
