from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView
)

from .models import Program, VrstaPrograma


class ProgramListView(ListView):
    model = Program

    def get_queryset(self):
        return Program.objects.filter(vrsta_programa_id=self.kwargs['vrsta_programa_id'])

    def get_context_data(self, **kwargs):
        context = super(ProgramListView, self).get_context_data(**kwargs)
        vp = VrstaPrograma.objects.get(id=self.kwargs['vrsta_programa_id'])
        context['title'] = vp.naziv
        return context
