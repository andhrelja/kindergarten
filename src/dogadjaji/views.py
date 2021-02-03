from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    PermissionRequiredMixin
)
from django.contrib import messages 

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.contrib.messages.views import SuccessMessageMixin

from .models import Dogadjaj
from .forms import DogadjajForm


# Create your views here.
class DogadjajListView(ListView):
    model = Dogadjaj

class DogadjajDetailView(DetailView):
    model = Dogadjaj


class DogadjajCreateView(
    LoginRequiredMixin, 
    # PermissionRequiredMixin, 
    UserPassesTestMixin, 
    SuccessMessageMixin, 
    CreateView
):
    model = Dogadjaj
    form_class = DogadjajForm
    success_message = 'Događaj uspješno spremljen'

    def get_context_data(self, **kwargs):
        context = super(DogadjajCreateView, self).get_context_data(**kwargs)
        context["title"] = "Novi događaj"
        return context
    
    def form_valid(self, form):
        vrste_programa = form.cleaned_data.get('vrste_programa')
        dogadjaj = form.save()
        for vp in vrste_programa:
            dogadjaj.vrstaprograma_set.add(vp)
        dogadjaj.inform_parents()
        dogadjaj.create_consents()
        return super(DogadjajCreateView, self).form_valid(form)

    def test_func(self): # TODO: Rewrite as permission
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        else:
            return False

class DogadjajUpdateView(
    LoginRequiredMixin, 
    # PermissionRequiredMixin, 
    UserPassesTestMixin, 
    SuccessMessageMixin, 
    UpdateView
):
    model = Dogadjaj
    form_class = DogadjajForm
    success_message = 'Događaj uspješno spremljen'

    def get_context_data(self, **kwargs):
        context = super(DogadjajUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Uredi događaj"
        return context
    
    def form_valid(self, form):
        vrste_programa = form.cleaned_data.get('vrste_programa')
        dogadjaj = form.save()
        for vp in vrste_programa:
            dogadjaj.vrstaprograma_set.add(vp)
        dogadjaj.create_consents()
        return super(DogadjajUpdateView, self).form_valid(form)

    def test_func(self): # TODO: Rewrite as permission
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        else:
            return False

class DogadjajDeleteView(
    LoginRequiredMixin, 
    # PermissionRequiredMixin, 
    UserPassesTestMixin, 
    SuccessMessageMixin, 
    DeleteView
):
    model = Dogadjaj
    success_message = 'Događaj uspješno izbrisan'
    success_url = '/dogadjaji/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DogadjajDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self): # TODO: Rewrite as permission
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        else:
            return False
