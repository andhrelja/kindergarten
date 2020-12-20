from django.views.generic.edit import UpdateView
from racuni.upisi.models import Upis
from racuni.models import Racun
from .forms import UpisForm, UpisCreateForm

from django.contrib.messages.views import SuccessMessageMixin
# from django.views.generic.edit import FormMixin
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)


class UpisCreateView(SuccessMessageMixin, CreateView):
    model = Upis
    form_class = UpisCreateForm
    template_name = 'upisi/upis_form.html'
    success_message = "Hvala Vam na poslanom zahtjevu!"
    "Kroz sljedećih 7 dana ćete dobiti povratnu informaciju putem pružene email adrese"
    

class UpisUpdateView(SuccessMessageMixin, UpdateView):
    model = Upis
    form_class = UpisForm
    template_name = 'upisi/upis_form.html'
    success_message = "Upis uspješno spremljen"

    def form_valid(self, form):
        roditelj = {
            'first_name': form.cleaned_data['roditelj_puno_ime'].split(" "),
            'email': form.cleaned_data['roditelj_email'],
            'telefon': form.cleaned_data['roditelj_telefon'],
            'datum_rodjenja': form.cleaned_data['datum_rodjenja'],
        }
        # roditelj = Racun.objects.create_user(**roditelj)
        dijete = {
            'ime': form.cleaned_data['ime'],
            'prezime': form.cleaned_data['prezime'],
            'datum_rodjenja': form.cleaned_data['datum_rodjenja'],
            'dodatne_informacije': form.cleaned_data['dodatne_informacije'],
            'roditelj': roditelj
        }
        return super(UpisUpdateView, self).form_valid(form)
    

class UpisDetailView(DetailView):
    model = Upis
    form_class = UpisForm
    template_name = "upisi/upis_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.odobren is not None:
            detail_form = UpisForm(instance=self.object)
        else:
            detail_form = UpisCreateForm(instance=self.object)
        detail_form.disable_fields()
        context['detail_form'] = detail_form
        return context


class UpisListView(ListView):
    model = Upis
    template_name = "upisi/upis_list.html"
