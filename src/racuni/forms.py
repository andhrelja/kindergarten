from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from racuni.models import Racun, TipRacuna

class DateInput(forms.DateInput):
    input_type = "date"

class TimeInput(forms.TimeInput):
    input_type = "time"


class LoginForm(AuthenticationForm):
    
    error_messages = {
        'invalid_login':
            "Unesite ispravan email i lozinku. Oba polja "
            "su osjetljiva na veličinu slova."
        ,
        'inactive': "Račun nije aktivan.",
    }

    def __init__(self, request, *args, **kwargs):
        super(LoginForm, self).__init__(request, *args, **kwargs)
        self.fields['username'].widget.attrs['class'] = "form-control"
        self.fields['password'].widget.attrs['class'] = "form-control"


class RacunForm(forms.ModelForm):

    error_messages = {
        'password_mismatch': 'Lozinke se ne podudaraju',
    }

    first_name  = forms.CharField(label="Ime", 
        max_length=128, 
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))
    last_name   = forms.CharField(label="Prezime", 
        max_length=128, 
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))
    email       = forms.EmailField(label="Email", 
        max_length=255, 
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control'
        }))
    password1   = forms.CharField(
        label="Lozinka",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password', 
            'class': 'form-control'
        })
    )
    password2   = forms.CharField(
        label="Potvrda lozinke",
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password', 
            'class': 'form-control'}
        ),
        strip=False,
        help_text="Unesite istu lozinku",
    )

    je_roditelj = forms.BooleanField(label="Roditelj", required=False, widget=forms.HiddenInput())
    je_djelatnik = forms.BooleanField(label="Djelatnik", required=False, widget=forms.HiddenInput())
    je_voditelj = forms.BooleanField(label="Voditelj", required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    je_strucni_tim = forms.BooleanField(label="Stručni tim", required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control'}))    

    class Meta:
        model = Racun
        fields = (
            'first_name', 
            'last_name', 
            'tip_racuna', 
            'je_voditelj', 
            'je_strucni_tim', 
            'telefon', 
            'datum_rodjenja', 
            'email', 
            'password1', 
            'password2', 
            'je_roditelj', 
            'je_djelatnik'
        )
        widgets = {
            'telefon':          forms.TextInput(attrs={'class': 'form-control'}),
            'datum_rodjenja':   DateInput(attrs={'class': 'form-control'}),
            'tip_racuna':       forms.Select(attrs={'class': 'custom-select'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(RacunForm, self).__init__(*args, **kwargs)
        je_djelatnik = kwargs['initial']['je_djelatnik']
        je_roditelj = kwargs['initial']['je_roditelj']

        self.fields['je_roditelj'].initial = je_roditelj
        self.fields['je_djelatnik'].initial = je_djelatnik

        if je_djelatnik and not je_roditelj:
            self.fields['tip_racuna'].queryset = TipRacuna.objects.filter(~Q(naziv="Roditelj"))
        elif not je_djelatnik and je_roditelj:
            self.fields['tip_racuna'].initial = TipRacuna.objects.get(naziv="Roditelj")
            self.fields['tip_racuna'].widget = forms.HiddenInput()
            self.fields['je_voditelj'].widget = forms.HiddenInput()
            self.fields['je_strucni_tim'].widget = forms.HiddenInput()
    
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        first_name = first_name.title()
        return first_name.strip()
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        last_name = last_name.title()
        return last_name.strip()
            
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
