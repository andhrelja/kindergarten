from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from django.views.generic import (
    ListView,
    TemplateView
)

from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta

from financije.models import Clanarina
import pytz


def get_daily_price(_date, vrsta_programa):
    num_month_days = get_num_month_days(_date)
    return vrsta_programa.clanstvo_cijena / num_month_days

def get_num_month_days(_date):
    if _date.month % 12 == 0:
        num_month_days = timezone.datetime(_date.year+1, 1, 1, tzinfo=pytz.UTC) - timezone.datetime(_date.year, _date.month, 1, tzinfo=pytz.UTC)
    else:
        num_month_days = timezone.datetime(_date.year, _date.month+1, 1, tzinfo=pytz.UTC) - timezone.datetime(_date.year, _date.month, 1, tzinfo=pytz.UTC)
    return num_month_days.days

# Create your views here.
class ClanarinaListView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    TemplateView
):
    template_name = "financije/financije_list.html"

    def get_context_data(self, **kwargs):
        context = super(ClanarinaListView, self).get_context_data(**kwargs)
        object_list = []
        start_date = self.request.user.racun.created_at
        end_date = timezone.now()

        first_day_next_month = timezone.datetime(start_date.year, start_date.month + 1, 1, 0, 0, tzinfo=pytz.UTC) if start_date.month % 12 != 0 else timezone.datetime(start_date.year + 1, 1, 1, 0, 0, tzinfo=pytz.UTC)
        first_month_total_days = (first_day_next_month - timedelta(days=1)) - start_date

        if start_date.year == end_date.year and start_date.month == end_date.month:
            daily_price = 0
            for dijete in self.request.user.racun.dijete_set.all():
                daily_price += get_daily_price(start_date, dijete.program.vrsta_programa)
            iznos = daily_price * first_month_total_days.days
            object_list.append(Clanarina(naziv="1", dijete=dijete, datum=end_date.date, iznos=iznos, PDV=iznos*0.25, ukupno=iznos*1.25))
        elif start_date.year == end_date.year and start_date.month != end_date.month:
            j = 0
            for i in range(start_date.month, end_date.month + 1):
                daily_price = 0
                for dijete in self.request.user.racun.dijete_set.all():
                    daily_price += get_daily_price(timezone.datetime(start_date.year, start_date.month + j, 1, 0, 0, tzinfo=pytz.UTC), dijete.program.vrsta_programa)
                iznos = daily_price * get_num_month_days(timezone.datetime(start_date.year, start_date.month + j, 1, 0, 0, tzinfo=pytz.UTC))
                object_list.append(Clanarina(naziv=str(j + 2), dijete=dijete, datum=end_date.date, iznos=iznos, PDV=iznos*0.25, ukupno=iznos*1.25))
        context.update({
            'object_list': object_list
        })
        return context
    
    def test_func(self):
        if self.request.user.racun and self.request.user.racun.tip_racuna.je_roditelj:
            return True
        else:
            return False