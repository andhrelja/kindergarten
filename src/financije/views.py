from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from django.views.generic import (
    TemplateView
)

from financije.models import Clanarina, Placa


# Create your views here.
class ClanarinaListView(
    LoginRequiredMixin,
    TemplateView
):
    template_name = "financije/financije_list.html"

    def get_context_data(self, **kwargs):
        context = super(ClanarinaListView, self).get_context_data(**kwargs)
        user = self.request.user
        self.get_or_create_objects(user)

        if user.is_superuser or (user.racun and user.racun.tip_racuna.je_voditelj):
            context = {
                'clanarina_list': Clanarina.objects.all(),
                'placa_list': Placa.objects.all()
            }
        elif user.racun and user.racun.tip_racuna.je_djelatnik:
            context = {
                'placa_list': Placa.objects.filter(djelatnik=user.racun)
            }
        elif user.racun and user.racun.tip_racuna.je_roditelj:
            context = {
                'clanarina_list': Clanarina.objects.filter(dijete__in=user.racun.dijete_set.all())
            }
        return context
    
    def get_or_create_objects(self, user):
        if user.is_superuser or (user.racun and user.racun.tip_racuna.je_voditelj):
            Clanarina().create_all()
            Placa.create_all()
        elif user.racun and user.racun.tip_racuna.je_djelatnik:
            Placa.create_one(djelatnik=user.racun)
        elif user.racun and user.racun.tip_racuna.je_roditelj:
            Clanarina.create_one(djeca=user.racun.dijete_set.all())
