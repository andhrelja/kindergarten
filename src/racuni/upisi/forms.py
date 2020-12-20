from django import forms
from racuni.forms import DateInput
from .models import Upis

class UpisForm(forms.ModelForm):
    
    class Meta:
        model = Upis
        fields = (
            'roditelj_puno_ime', 
            'roditelj_email', 
            'roditelj_datum_rodjenja', 
            'roditelj_telefon', 
            'dijete_puno_ime', 
            'dijete_datum_rodjenja', 
            'odobren', 
            'obrazlozenje' 
        )

        widgets = {
            'roditelj_puno_ime': forms.TextInput(attrs={'class': 'form-control'}),
            'roditelj_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'roditelj_datum_rodjenja': DateInput(attrs={'class': 'form-control'}),
            'roditelj_telefon': forms.TextInput(attrs={'class': 'form-control'}),
            'dijete_puno_ime': forms.TextInput(attrs={'class': 'form-control'}),
            'dijete_datum_rodjenja': DateInput(attrs={'class': 'form-control'}),
            'odobren': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'obrazlozenje': forms.Textarea(attrs={'class': 'form-control'}),
        }
    
    def disable_fields(self, enable=None):
        for field_name, field in self.fields.items():
            field.required = False
            field.disabled = True

            if enable and enable == field_name:
                field.required = True
                field.disabled = False
                field.widget.attrs.update({'autofocus': True})
            elif enable and enable != field_name:
                field.widget = forms.HiddenInput()

class UpisCreateForm(UpisForm):

    class Meta(UpisForm.Meta):
        fields = (
            'roditelj_puno_ime', 
            'roditelj_email', 
            'roditelj_datum_rodjenja', 
            'roditelj_telefon', 
            'dijete_puno_ime', 
            'dijete_datum_rodjenja'
        )
