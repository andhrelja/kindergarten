from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView

from .models import Racun, TipRacuna
from .forms import LoginForm, RacunForm, RacunUpdateForm


# Generic views

class LoginView(LoginView):
    form_class = LoginForm


class RacunListView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    ListView
):
    model = Racun
    template_name = "racuni/racun_list.html"

    def test_func(self): # TODO: Rewrite as permission
        if self.request.user.is_staff:
            return True
        else:
            return False


class RacunDetailView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DetailView
):
    model = Racun

    def test_func(self): # TODO: Rewrite as permission
        self.object = self.get_object()
        if (self.request.user.is_staff 
            or (self.object == self.request.user.racun
            and self.request.user.racun)):
            return True
        else:
            return False

class DjelatnikCreateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    CreateView
):
    model = Racun
    form_class = RacunForm

    def get_form_kwargs(self):
        kwargs = super(DjelatnikCreateView, self).get_form_kwargs()
        kwargs['tip'] = "djelatnik"
        return kwargs
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        user_kwargs = {
            'first_name': form.cleaned_data['first_name'],
            'last_name': form.cleaned_data['last_name'],
            'email': form.cleaned_data['email'],
            'password': form.cleaned_data['password2'],
            'is_staff': True,
        }
        
        user = Racun.objects.create_user(**user_kwargs)
        self.object.user = user
        self.object.save()

        messages.success(self.request, "Djelatnik uspješno spremljen")
        return redirect(self.object.get_absolute_url())
    
    def get_context_data(self, **kwargs):
        context = super(DjelatnikCreateView, self).get_context_data(**kwargs)
        context['form_title'] = "Dodaj djelatnika"
        return context

    def test_func(self): # TODO: Rewrite as permission
        if (self.request.user.is_superuser 
            or (self.request.user.racun.tip_racuna.je_voditelj
            and self.request.user.racun)):
            return True
        else:
            return False


class RoditeljCreateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    CreateView
):
    model = Racun
    form_class = RacunForm

    def get_initial(self):
        initial = super(RoditeljCreateView, self).get_initial()
        initial['tip_racuna'] = TipRacuna.objects.get(naziv="Roditelj")
        return initial
    
    def get_form_kwargs(self):
        kwargs = super(RoditeljCreateView, self).get_form_kwargs()
        kwargs['tip'] = "roditelj"
        return kwargs
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        user_kwargs = {
            'first_name': form.cleaned_data['first_name'],
            'last_name': form.cleaned_data['last_name'],
            'email': form.cleaned_data['email'],
            'password': form.cleaned_data['password2'],
        }
        
        user = Racun.objects.create_user(**user_kwargs)
        self.object.user = user
        self.object.save()

        messages.success(self.request, "Roditelj uspješno spremljen")
        return redirect(self.object.get_absolute_url())
    
    def get_context_data(self, **kwargs):
        context = super(RoditeljCreateView, self).get_context_data(**kwargs)
        context['form_title'] = "Dodaj roditelja"
        return context

    def test_func(self): # TODO: Rewrite as permission
        if (self.request.user.is_superuser 
            or (self.request.user.racun.tip_racuna.je_voditelj
            and self.request.user.racun)):
            return True
        else:
            return False


class DjelatnikUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):
    model = Racun
    form_class = RacunUpdateForm

    def get_initial(self):
        initial = super(DjelatnikUpdateView, self).get_initial()
        initial.update({
            'first_name': self.object.user.first_name,
            'last_name': self.object.user.last_name,
            'email': self.object.user.email
        })
        return initial

    def get_form_kwargs(self):
        kwargs = super(DjelatnikUpdateView, self).get_form_kwargs()
        kwargs['tip'] = "djelatnik"
        return kwargs
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        
        self.object.user.first_name = form.cleaned_data.pop('first_name')
        self.object.user.last_name = form.cleaned_data.pop('last_name')
        self.object.user.email = form.cleaned_data.pop('email')
        self.object.user.is_staff = True
        self.object.user.save()
        form.save()

        messages.success(self.request, "Djelatnik uspješno spremljen")
        return redirect(self.object.get_absolute_url())
    
    def get_context_data(self, **kwargs):
        context = super(DjelatnikUpdateView, self).get_context_data(**kwargs)
        context['form_title'] = "Uredi djelatnika"
        return context

    def test_func(self): # TODO: Rewrite as permission
        if (self.request.user.is_superuser 
            or (self.request.user.racun.tip_racuna.je_voditelj
            and self.request.user.racun)):
            return True
        else:
            return False


class RoditeljUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):
    model = Racun
    form_class = RacunUpdateForm

    def get_initial(self):
        initial = super(RoditeljUpdateView, self).get_initial()
        initial.update({
            'tip_racuna': TipRacuna.objects.get(naziv="Roditelj"),
            'first_name': self.object.user.first_name,
            'last_name': self.object.user.last_name,
            'email': self.object.user.email
        })
        return initial
    
    def get_form_kwargs(self):
        kwargs = super(RoditeljUpdateView, self).get_form_kwargs()
        kwargs['tip'] = "roditelj"
        return kwargs
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        
        self.object.user.first_name = form.cleaned_data.pop('first_name')
        self.object.user.last_name = form.cleaned_data.pop('last_name')
        self.object.user.email = form.cleaned_data.pop('email')
        self.object.user.save()
        form.save()

        messages.success(self.request, "Roditelj uspješno spremljen")
        return redirect(self.object.get_absolute_url())
    
    def get_context_data(self, **kwargs):
        context = super(RoditeljUpdateView, self).get_context_data(**kwargs)
        context['form_title'] = "Uredi roditelja"
        return context

    def test_func(self): # TODO: Rewrite as permission
        if (self.request.user.is_superuser 
            or (self.request.user.racun.tip_racuna.je_voditelj
            and self.request.user.racun)):
            return True
        else:
            return False


class RacunDeleteView(
    LoginRequiredMixin, 
    # PermissionRequiredMixin, 
    UserPassesTestMixin, 
    SuccessMessageMixin, 
    DeleteView
):
    model = Racun
    success_message = 'Račun uspješno izbrisan'
    success_url = '/racuni/'


    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(RacunDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self): # TODO: Rewrite as permission
        if (self.request.user.is_superuser 
            or (self.request.user.racun.tip_racuna.je_voditelj
            and self.request.user.racun)):
            return True
        else:
            return False
