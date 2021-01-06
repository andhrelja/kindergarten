from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    PermissionRequiredMixin
)

from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from djeca.models import Dijete
from .models import DijeteNapredak
from .forms import DijeteNapredakForm


class NapredakCreateView(
    LoginRequiredMixin, 
    # PermissionRequiredMixin, 
    UserPassesTestMixin, 
    SuccessMessageMixin, 
    CreateView
):
    model = DijeteNapredak
    form_class = DijeteNapredakForm
    success_message = "Napredak uspješno zabilježen"
    template_name = "djeca/napredak/napredak_form.html"

    # permission_required = ('add_dijetenapredak', )

    def get_context_data(self, **kwargs):
        context = super(NapredakCreateView, self).get_context_data(**kwargs)

        dijete_id = self.kwargs.get('dijete_pk')
        context["dijete"] = Dijete.objects.get(id=dijete_id)
        context["title"] = "Novi zapis o napretku djeteta"
        return context
    
    def get_initial(self):
        initial = super(NapredakCreateView, self).get_initial()
        dijete_id = self.kwargs.get('dijete_pk')
        initial["dijete"] = Dijete.objects.get(id=dijete_id)
        return initial
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.autor = self.request.user
        self.object.save()
        return super(NapredakCreateView, self).form_valid(form)

    
    def test_func(self): # TODO: Rewrite as permission
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        else:
            return False