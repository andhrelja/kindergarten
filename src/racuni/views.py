from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    PermissionRequiredMixin
)

from django.contrib import messages 

from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from .models import Racun, TipRacuna
from .forms import LoginForm, RacunForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class LoginView(LoginView):
    form_class = LoginForm


class DjelatnikCreateView(CreateView):
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
        context = super().get_context_data(**kwargs)
        context['form_title'] = "Dodaj djelatnika"
        return context


class RoditeljCreateView(CreateView):
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
        context = super().get_context_data(**kwargs)
        context['form_title'] = "Dodaj roditelja"
        return context

class RacunListView(ListView):
    model = Racun
    template_name = "racuni/racun_list.html"


class RacunDetailView(DetailView):
    model = Racun


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
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        else:
            return False
