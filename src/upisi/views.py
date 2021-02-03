from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    ListView,
)

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect

from racuni.models import Racun, TipRacuna
from programi.models import VrstaPrograma
from djeca.models import Dijete
from .models import Upis
from .forms import UpisForm, UpisCreateForm


# Generic views

class UpisListView(ListView):
    model = Upis


class UpisDetailView(DetailView):
    model = Upis
    form_class = UpisForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.odobren is True:
            detail_form = UpisForm(instance=self.object, initial={'vrsta_programa': VrstaPrograma.objects.get(program=self.object.program)})
        else:
            detail_form = UpisCreateForm(instance=self.object, initial={'vrsta_programa': VrstaPrograma.objects.get(program=self.object.program)})
        detail_form.disable_fields()
        context['detail_form'] = detail_form
        return context


class UpisCreateView(SuccessMessageMixin, CreateView):
    model = Upis
    form_class = UpisCreateForm
    success_message = "Hvala Vam na poslanom zahtjevu!"
    "Kroz sljedećih 7 dana ćete dobiti povratnu informaciju putem pružene email adrese"
    

class UpisUpdateView(UpdateView):
    model = Upis
    form_class = UpisForm
    template_name = 'upisi/upis_confirm_form.html'

    def get_context_data(self, **kwargs):
        context = super(UpisUpdateView, self).get_context_data(**kwargs)
        context['vrsta_programa'] = VrstaPrograma.objects.get(program=self.object.program)
        context['program'] = self.object.program
        return context
    
    def get_initial(self):
        initial = super(UpisUpdateView, self).get_initial()
        vrsta_programa = VrstaPrograma.objects.get(program=self.object.program)
        initial['vrsta_programa'] = vrsta_programa
        return initial

    def form_valid(self, form):
        self.object = form.save()
        if self.object.odobren:
            user_kwargs = {
                'first_name': self.object.roditelj_puno_ime.split(" ")[0].title(),
                'last_name': self.object.roditelj_puno_ime.split(" ")[1].title(),
            }
            email = self.object.roditelj_email
            password = form.cleaned_data['password2']
            _, roditelj_korisnik = Racun.objects.get_or_create_user(email, password, **user_kwargs)
            
            roditelj = {
                'telefon': self.object.roditelj_telefon,
                'datum_rodjenja': self.object.roditelj_datum_rodjenja
            }
            tip_racuna = TipRacuna.objects.get(naziv="Roditelj")
            roditelj, _ = Racun.objects.get_or_create(user=roditelj_korisnik, tip_racuna=tip_racuna, **roditelj)

            dijete = {
                'ime': self.object.dijete_puno_ime.split(" ")[0],
                'prezime': self.object.dijete_puno_ime.split(" ")[1],
                'datum_rodjenja': self.object.dijete_datum_rodjenja,
                'dodatne_informacije': self.object.dijete_dodatne_informacije,
                'roditelj': roditelj,
                'program': self.object.program
            }
            Dijete.objects.get_or_create(**dijete)
            messages.success(self.request, "Zahtjev za upisom je odobren. Poslana je obavijest e-mailom")
            return redirect('racuni:popis')
        elif not self.object.odobren:
            messages.success(self.request, "Zahtjev za upisom je odbijen. Poslana je obavijest e-mailom")
            return super(UpisUpdateView, self).form_valid(form)
