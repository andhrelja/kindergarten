from django.views.generic import (
    ListView,
    TemplateView
)

from djeca.models import DobnaSkupina
from smjene.models import Smjena
from .mixins import JSONResponseMixin
from .models import Program, VrstaPrograma


# Generic views

class VrstaProgramaListView(ListView):
    model = VrstaPrograma


class ProgramListView(ListView):
    model = Program

    def get_queryset(self):
        return Program.objects.filter(vrsta_programa_id=self.kwargs['vrsta_programa_id'])

    def get_context_data(self, **kwargs):
        context = super(ProgramListView, self).get_context_data(**kwargs)
        vp = VrstaPrograma.objects.get(id=self.kwargs['vrsta_programa_id'])
        context['title'] = vp.naziv
        return context


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
    
class ProgramUpisanoDjeceJSONView(JSONResponseMixin, TemplateView):
    def render_to_response(self, context, **response_kwargs):
        program_id = self.kwargs.get('program_id', None)
        program = Program.objects.get(id=program_id)
        response_kwargs.update({
            'upisano_djece': program.dijete_set.count(),
            'max_broj_djece': program.max_broj_djece
        })
        return self.render_to_json_response(context, **response_kwargs)

class ProgramSmjenaCijenaJSONView(JSONResponseMixin, TemplateView):
    def render_to_response(self, context, **response_kwargs):
        program_id = self.kwargs.get('program_id', None)
        smjena_id = self.kwargs.get('smjena_id', None)
        program = Program.objects.get(id=program_id)
        smjena = Smjena.objects.get(id=smjena_id)
        response_kwargs.update({
            'clanstvo': program.vrsta_programa.clanstvo_cijena,
            'broj_sati': smjena.broj_sati()
        })
        return self.render_to_json_response(context, **response_kwargs)
    