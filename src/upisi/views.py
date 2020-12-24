from .models import Upis
from racuni.models import Racun, TipRacuna
from djeca.models import Dijete
from .forms import UpisForm, UpisCreateForm

# from django.views.generic.edit import FormMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    ListView,
)


class UpisCreateView(SuccessMessageMixin, CreateView):
    model = Upis
    form_class = UpisCreateForm
    success_message = "Hvala Vam na poslanom zahtjevu!"
    "Kroz sljedećih 7 dana ćete dobiti povratnu informaciju putem pružene email adrese"
    

class UpisUpdateView(UpdateView):
    model = Upis
    form_class = UpisForm

    def get_context_data(self, **kwargs):
        context =  super(UpisUpdateView, self).get_context_data(**kwargs)
        context['update'] = True
        return context

    def form_valid(self, form):
        form.save()
        odobren = form.cleaned_data['odobren']
        if odobren and form.cleaned_data['password2']:
            user_kwargs = {
                'first_name': form.cleaned_data['roditelj_puno_ime'].split(" ")[0],
                'last_name': form.cleaned_data['roditelj_puno_ime'].split(" ")[1],
            }
            email = form.cleaned_data.pop('roditelj_email')
            password = form.cleaned_data.pop('password2')
            _, roditelj_korisnik = Racun.objects.get_or_create_user(email, password, **user_kwargs)
            
            roditelj = {
                'telefon': form.cleaned_data['roditelj_telefon'],
                'datum_rodjenja': form.cleaned_data['roditelj_datum_rodjenja'],
                'je_roditelj': True,
                'je_djelatnik': False,
                'je_voditelj': False,
                'je_strucni_tim': False
            }
            tip_racuna = TipRacuna.objects.get(naziv="Roditelj")
            roditelj, _ = Racun.objects.get_or_create(user=roditelj_korisnik, tip_racuna=tip_racuna, **roditelj)

            dijete = {
                'ime': form.cleaned_data['dijete_puno_ime'].split(" ")[0],
                'prezime': form.cleaned_data['dijete_puno_ime'].split(" ")[1],
                'datum_rodjenja': form.cleaned_data['dijete_datum_rodjenja'],
                'dodatne_informacije': form.cleaned_data['dijete_dodatne_informacije'],
                'roditelj': roditelj
            }
            Dijete.objects.get_or_create(**dijete)
            messages.success(self.request, "Roditelj uspješno spremljen. Poslana je obavijest e-mailom")
            return redirect('racuni:popis')
        elif odobren and not form.cleaned_data['password2']:
            messages.warning(self.request, "Kod odobrenog zahtjeva za upis potrebno je unijeti lozinku za korisnika")
            return super(UpisUpdateView, self).form_invalid(form)
        elif not odobren:
            messages.success(self.request, "Roditelj nije spremljen. Poslana je obavijest e-mailom")
            return super(UpisUpdateView, self).form_valid(form)
    

class UpisDetailView(DetailView):
    model = Upis
    form_class = UpisForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.odobren is True:
            detail_form = UpisForm(instance=self.object)
        else:
            detail_form = UpisCreateForm(instance=self.object)
        detail_form.disable_fields()
        context['detail_form'] = detail_form
        return context


class UpisListView(ListView):
    model = Upis
