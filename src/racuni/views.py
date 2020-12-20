from django.contrib.auth.views import LoginView, LogoutView
from .models import Racun, TipRacuna
from .forms import LoginForm, RacunForm
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView
)


class LoginView(LoginView):
    form_class = LoginForm


class DjelatnikCreateView(CreateView):
    model = Racun
    form_class = RacunForm

    def get_initial(self):
        initial = super(DjelatnikCreateView, self).get_initial()
        initial['je_djelatnik'] = True
        return initial

class RoditeljCreateView(CreateView):
    model = Racun
    form_class = RacunForm

    def get_initial(self):
        initial = super(RoditeljCreateView, self()).get_initial()
        initial['je_roditelj'] = True
        initial['tip_racuna'] = TipRacuna.objects.get(name="Roditelj")
        return initial

class RacunListView(ListView):
    model = Racun
    template_name = "racuni/racun_list.html"
