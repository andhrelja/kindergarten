from django import forms
from .models import Dogadjaj
from racuni.forms import DateInput, TimeInput
from programi.models import VrstaPrograma

class DogadjajForm(forms.ModelForm):
    vrste_programa = forms.ModelMultipleChoiceField(
        label="Vrsta programa", 
        queryset=VrstaPrograma.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Dogadjaj
        fields = ('vrste_programa', 'naziv', 'opis', 'adresa', 'datum_start', 'datum_kraj', 'vrijeme_start', 'vrijeme_kraj')
        widgets = {
            'naziv': forms.TextInput(attrs={'class': 'form-control'}),
            'opis': forms.Textarea(attrs={'class': 'form-control'}),
            'adresa': forms.TextInput(attrs={'class': 'form-control'}),
            'datum_start': DateInput(attrs={'class': 'form-control'}),
            'datum_kraj': DateInput(attrs={'class': 'form-control'}),
            'vrijeme_start': TimeInput(attrs={'class': 'form-control'}),
            'vrijeme_kraj': TimeInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(DogadjajForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            self.fields['vrste_programa'].initial = kwargs['instance'].vrstaprograma_set.all()