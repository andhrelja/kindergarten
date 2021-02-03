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

from dogadjaji.models import Dogadjaj
from .models import Suglasnost
from .forms import SuglasnostForm


# Generic views

class SuglasnostListView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    ListView
):
    model = Suglasnost
    template_name = "dogadjaji/suglasnosti/suglasnost_list.html"

    def get_queryset(self):
        dogadjaj = Dogadjaj.objects.get(pk=self.kwargs.get('dogadjaj_pk'))
        return Suglasnost.objects.filter(dogadjaj=dogadjaj)

    def test_func(self): # TODO: Rewrite as permission
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        else:
            return False


class SuglasnostDetailView(
    LoginRequiredMixin, 
    UserPassesTestMixin,
    DetailView
):
    model = Suglasnost
    template_name = "dogadjaji/suglasnosti/suglasnost_detail.html"

    def get_object(self):
        return Suglasnost.objects.get(pk=self.kwargs.get('suglasnost_pk'))
    
    def test_func(self): # TODO: Rewrite as permission
        object = self.get_object()
        if self.request.user.is_staff or object.dijete in self.request.user.racun.dijete_set.all():
            return True
        else:
            return False


class SuglasnostCreateView(
    LoginRequiredMixin, 
    SuccessMessageMixin, 
    CreateView
):
    model = Suglasnost
    form_class = SuglasnostForm
    success_message = 'Suglasnost uspješno spremljena'
    template_name = "dogadjaji/suglasnosti/suglasnost_form.html"


    def get_context_data(self, **kwargs):
        context = super(SuglasnostCreateView, self).get_context_data(**kwargs)
        context["title"] = "Nova suglasnost"
        return context
    

class SuglasnostUpdateView(
    LoginRequiredMixin, 
    SuccessMessageMixin, 
    UpdateView
):
    model = Suglasnost
    form_class = SuglasnostForm
    success_message = 'Suglasnost uspješno spremljena'
    template_name = "dogadjaji/suglasnosti/suglasnost_form.html"


    def get_object(self):
        return Suglasnost.objects.get(pk=self.kwargs.get('suglasnost_pk'))

    def get_context_data(self, **kwargs):
        context = super(SuglasnostUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Uredi suglasnost"
        return context
    

class SuglasnostDeleteView(
    LoginRequiredMixin, 
    # PermissionRequiredMixin, 
    UserPassesTestMixin,
    DeleteView
):
    model = Suglasnost
    success_message = 'Suglasnost uspješno izbrisana'
    success_url = '/dogadjaji/suglasnosti/'
    template_name = "dogadjaji/suglasnosti/suglasnost_confirm_delete.html"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(SuglasnostDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self): # TODO: Rewrite as permission
        if self.request.user.is_staff:
            return True
        else:
            return False
