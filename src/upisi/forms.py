from django import forms
from racuni.forms import DateInput
from .models import Upis


class UpisForm(forms.ModelForm):
    
    error_messages = {
        'email_exists': "Zahtjev s upisanim e-mailom već postoji"
    }

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
            'roditelj_datum_rodjenja': DateInput(attrs={'class': 'form-control'}),
            'roditelj_telefon': forms.TextInput(attrs={'class': 'form-control'}),
            'dijete_puno_ime': forms.TextInput(attrs={'class': 'form-control'}),
            'dijete_datum_rodjenja': DateInput(attrs={'class': 'form-control'}),
            'dijete_dodatne_informacije': forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
            'odobren': forms.CheckboxInput(attrs={'class': 'form-control', 'onclick': 'switchDisplay()'}),
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
    
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Lozinke se ne podudaraju')
        return password2


class UpisCreateForm(UpisForm):

    class Meta(UpisForm.Meta):
        fields = (
            'roditelj_puno_ime', 
            'roditelj_email', 
            'roditelj_datum_rodjenja', 
            'roditelj_telefon', 
            'dijete_puno_ime', 
            'dijete_datum_rodjenja',
            'dijete_dodatne_informacije'
        )
