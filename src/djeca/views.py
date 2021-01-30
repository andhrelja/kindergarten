from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)

from .models import Dijete
from .forms import DijeteForm


class DijeteListView(ListView):
    model = Dijete

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser and user.racun.je_roditelj:
            return Dijete.objects.filter(roditelj=user.racun)
        else:
            return super(DijeteListView, self).get_queryset()
    


class DijeteDetailView(DetailView):
    model = Dijete


class DijeteUpdateView(UpdateView):
    model = Dijete
    form_class = DijeteForm
