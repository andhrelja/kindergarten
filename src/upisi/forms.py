from django import forms

from racuni.forms import DateInput
from programi.models import VrstaPrograma, Program
from smjene.models import Smjena
from .models import Upis

from datetime import datetime


class UpisForm(forms.ModelForm):
    
    error_messages = {
        'email_exists': "Zahtjev s upisanim e-mailom već postoji"
    }

    vrsta_programa = forms.ModelChoiceField(
        label="Vrsta programa", 
        queryset=VrstaPrograma.objects.all(),
        widget=forms.Select(attrs={
            'class': 'custom-select'
        })
    )
    
    password1   = forms.CharField(
        label="Lozinka za korisnika",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password', 
            'class': 'form-control'
        }),
        required=False
    )
    password2   = forms.CharField(
        label="Potvrda lozinke",
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password', 
            'class': 'form-control'}
        ),
        strip=False,
        help_text="Unesite istu lozinku",
        required=False
    )


    class Meta:
        model = Upis
        fields = (
            'vrsta_programa',
            'program',
            'smjena',
            'roditelj_puno_ime', 
            'roditelj_email', 
            'roditelj_datum_rodjenja', 
            'roditelj_telefon', 
            'dijete_puno_ime', 
            'dijete_datum_rodjenja', 
            'dijete_dodatne_informacije', 
            'odobren', 
            'obrazlozenje',
            'password1',
            'password2'
        )

        widgets = {
            'roditelj_puno_ime': forms.TextInput(attrs={'class': 'form-control'}),
            'roditelj_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'program': forms.Select(attrs={'class': 'custom-select'}),
            'smjena': forms.Select(attrs={'class': 'custom-select'}),
            'roditelj_datum_rodjenja': DateInput(attrs={'class': 'form-control'}),
            'roditelj_telefon': forms.TextInput(attrs={'class': 'form-control'}),
            'dijete_puno_ime': forms.TextInput(attrs={'class': 'form-control'}),
            'dijete_datum_rodjenja': DateInput(attrs={'class': 'form-control'}),
            'dijete_dodatne_informacije': forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
            'odobren': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'obrazlozenje': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
        }


    def disable_fields(self):
        for _, field in self.fields.items():
            field.required = False
            field.disabled = True

    def clean_program(self):
        program = self.cleaned_data.get('program')
        if program.dijete_set.count() >= program.max_broj_djece:
            self.add_error('program', 'Kapacitet programa je popunjen. Molimo odaberite drugi program')
        return program

    def clean_dijete_datum_rodjenja(self):
        program = self.cleaned_data.get('program')
        datum_rodjenja = self.cleaned_data.get("dijete_datum_rodjenja")
        tdelta = datetime.now() - datetime(datum_rodjenja.year, datum_rodjenja.month, datum_rodjenja.day, 0, 0)
        godine = tdelta.days / 365
        ds_min = program.dobne_skupine.order_by('godine_min').first()
        ds_max = program.dobne_skupine.order_by('godine_min').last()
        
        if godine >= ds_min.godine_min and godine <= ds_max.godine_max:
            return datum_rodjenja
        self.add_error('dijete_datum_rodjenja', 'Dijete ne pripada odabranoj dobnoj skupini')

    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Lozinke se ne podudaraju')
        return password2


class UpisCreateForm(UpisForm):

    class Meta(UpisForm.Meta):
        fields = (
            'vrsta_programa',
            'program',
            'smjena',
            'roditelj_puno_ime', 
            'roditelj_email', 
            'roditelj_datum_rodjenja', 
            'roditelj_telefon', 
            'dijete_puno_ime', 
            'dijete_datum_rodjenja',
            'dijete_dodatne_informacije'
        )

    def __init__(self, *args, **kwargs):
        roditelj = kwargs.pop('roditelj', None)
        super(UpisCreateForm, self).__init__(*args, **kwargs)
        
        if roditelj:
            for key, field in self.fields.items():
                if key.startswith('roditelj'):
                    field.disabled = True
                    if key.endswith('email'):
                        field.help_text = None