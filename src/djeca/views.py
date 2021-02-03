from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Dijete
from .forms import DijeteForm


# Generic views

class DijeteListView(ListView):
    model = Dijete

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser and user.racun.tip_racuna.je_roditelj:
            return Dijete.objects.filter(roditelj=user.racun)
        else:
            return super(DijeteListView, self).get_queryset()


class DijeteDetailView(DetailView):
    model = Dijete


class DijeteUpdateView(SuccessMessageMixin, UpdateView):
    model = Dijete
    form_class = DijeteForm
    success_message = "Dijete uspješno spremljeno"


class DijeteDeleteView(
    LoginRequiredMixin, 
    UserPassesTestMixin,
    DeleteView
):
    model = Dijete
    success_message = 'Dijete uspješno izbrisano'
    success_url = '/djeca/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DijeteDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self): # TODO: Rewrite as permission
        if self.request.user.is_staff:
            return True
        else:
            return False
