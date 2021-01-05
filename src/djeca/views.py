from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Dijete


class DijeteListView(ListView):
    model = Dijete

    def get_queryset(self):
        user = self.request.user
        if user.racun.je_roditelj:
            return Dijete.objects.filter(roditelj=user.racun)
        else:
            return super(DijeteListView, self).get_queryset()
    


class DijeteDetailView(DetailView):
    model = Dijete