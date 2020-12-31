from django.views.generic import (
    ListView,
    DetailView,
    TemplateView
)

from .mixins import JSONResponseMixin
from .models import Program, VrstaPrograma
from djeca.models import DobnaSkupina
from smjene.models import Smjena


class ProgramListView(ListView):
    model = Program

    def get_queryset(self):
        return Program.objects.filter(vrsta_programa_id=self.kwargs['vrsta_programa_id'])

    def get_context_data(self, **kwargs):
        context = super(ProgramListView, self).get_context_data(**kwargs)
        vp = VrstaPrograma.objects.get(id=self.kwargs['vrsta_programa_id'])
        context['title'] = vp.naziv
        return context


class VrstaProgramaListView(ListView):
    model = VrstaPrograma


class VrstaProgramaJSONView(JSONResponseMixin, TemplateView):
    def render_to_response(self, context, **response_kwargs):
        vrsta_programa_id = self.kwargs.get('vrsta_programa_id', None)
        queryset = VrstaPrograma.objects.filter(id=vrsta_programa_id)
        return self.render_to_json_response(context, queryset=queryset, safe=False)
    
class ProgramiJSONView(JSONResponseMixin, TemplateView):
    def render_to_response(self, context, **response_kwargs):
        vrsta_programa_id = self.kwargs.get('vrsta_programa_id', None)
        queryset = Program.objects.filter(vrsta_programa_id=vrsta_programa_id)
        return self.render_to_json_response(context, queryset=queryset, safe=False)


class ProgramDobneSkupineJSONView(JSONResponseMixin, TemplateView):
    def render_to_response(self, context, **response_kwargs):
        program_id = self.kwargs.get('program_id', None)
        program = Program.objects.get(id=program_id)
        queryset = DobnaSkupina.objects.filter(program=program)
        return self.render_to_json_response(context, queryset=queryset, safe=False)

class ProgramSmjeneJSONView(JSONResponseMixin, TemplateView):
    def render_to_response(self, context, **response_kwargs):
        program_id = self.kwargs.get('program_id', None)
        program = Program.objects.get(id=program_id)
        queryset = Smjena.objects.filter(program=program)
        return self.render_to_json_response(context, queryset=queryset, safe=False)
    
