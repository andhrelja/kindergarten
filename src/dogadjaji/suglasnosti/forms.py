from django import forms
from .models import Suglasnost

class SuglasnostForm(forms.ModelForm):
    
    class Meta:
        model = Suglasnost
        fields = ("odobren",)
        widgets = {
            "odobren": forms.CheckboxInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(SuglasnostForm, self).__init__(*args, **kwargs)
        self.fields['odobren'].label = "Jeste li sigurni da želite dati suglasnost za prisustvovanje djeteta u događaju?"