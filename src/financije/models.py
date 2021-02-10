from django.db import models
from django.db.models import Q
from django.utils import timezone
from djeca.models import Dijete
from racuni.models import Racun, TipRacuna

from datetime import datetime
import pytz


class Clanarina(models.Model):

    # Atributi
    naziv  = models.CharField("Naziv dokumenta", max_length=128)
    datum  = models.DateField("Datum dokumenta")
    iznos  = models.FloatField("Iznos")
    PDV    = models.FloatField("PDV")
    ukupno = models.FloatField("Ukupno")

    # Vanjski ključevi
    dijete = models.ForeignKey("djeca.Dijete", verbose_name="Dijete", on_delete=models.CASCADE)
    created_at = models.DateTimeField("Datum stvaranja", auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "Članarina"
        verbose_name_plural = "Članarine"
        ordering = ['-datum']        
    
    @staticmethod
    def create_all():
        djeca = Dijete.objects.all()
        now = timezone.now()
        for dijete in djeca:
            range_start = 0
            time_since = now - dijete.roditelj.created_at
            months_since = int(time_since.days / 30)
            if now.day < 15:
                range_start = 1
            month = now.month
            year = now.year
            for i in range(range_start, months_since):
                if i % 12 == now.month:
                    month = 12
                    year -= 1
                else:
                    month -= (i % 12)

                kwargs = {
                    'datum' : datetime(year, month, 15, 0, 0, tzinfo=pytz.UTC),
                    'naziv' : "{} - {}".format(i + 1, dijete.get_full_name()),
                    'iznos' : dijete.program.vrsta_programa.clanstvo_mjesecno(dijete.smjena)
                }
                kwargs.update({
                    'PDV' : kwargs['iznos'] * 0.25,
                    'ukupno' : kwargs['iznos'] * 1.25
                })
                

                try:
                    Clanarina.objects.get(dijete=dijete, datum=kwargs.get('datum'))
                except Clanarina.DoesNotExist:
                    Clanarina.objects.create(dijete=dijete, **kwargs)
                

    @staticmethod
    def create_one(djeca):
        now = timezone.now()
        for dijete in djeca:
            range_start = 0
            time_since = now - dijete.roditelj.created_at
            months_since = int(time_since.days / 30)
            if now.day < 15:
                range_start = 1
            month = now.month
            year = now.year
            for i in range(range_start, months_since):
                if i % 12 == now.month:
                    month = 12
                    year -= 1
                else:
                    month -= (i % 12)

                kwargs = {
                    'datum' : datetime(year, month, 15, 0, 0, tzinfo=pytz.UTC),
                    'naziv' : "C{} - {}".format(i + 1, dijete.get_full_name()),
                    'iznos' : dijete.program.vrsta_programa.clanstvo_mjesecno(dijete.smjena)
                }
                kwargs.update({
                    'PDV' : kwargs['iznos'] * 0.25,
                    'ukupno' : kwargs['iznos'] * 1.25
                })
                

                try:
                    Clanarina.objects.get(dijete=dijete, datum=kwargs.get('datum'))
                except Clanarina.DoesNotExist:
                    Clanarina.objects.create(dijete=dijete, **kwargs)

    def __str__(self):
        return self.naziv


class Placa(models.Model):

    # Atributi
    naziv     = models.CharField("Naziv dokumenta", max_length=50)
    datum     = models.DateField("Datum dokumenta")
    bruto     = models.FloatField("Bruto iznos plaće")
    neto      = models.FloatField("Neto iznos plaće")
    
    # Vanjski ključevi
    djelatnik = models.ForeignKey("racuni.Racun", verbose_name="Djelatnik", on_delete=models.CASCADE)
    created_at = models.DateTimeField("Datum stvaranja", auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = "Plaća"
        verbose_name_plural = "Plaće"
        ordering = ['-datum']

    @staticmethod
    def create_all():
        tipovi = TipRacuna.objects.filter(Q(je_djelatnik=True) | Q(je_voditelj=True))
        djelatnici = Racun.objects.filter(tip_racuna__in=tipovi)
        now = timezone.now()
        for djelatnik in djelatnici:
            range_start = 0
            time_since = now - djelatnik.created_at
            months_since = int(time_since.days / 30)
            if now.day < 15:
                range_start = 1
            month = now.month
            year = now.year
            for i in range(range_start, months_since):
                if i % 12 == now.month:
                    month = 12
                    year -= 1
                else:
                    month -= (i % 12)

                kwargs = {
                    'datum' : datetime(year, month, 15, 0, 0, tzinfo=pytz.UTC),
                    'naziv' : "{} - {}".format(i + 1, djelatnik.get_full_name()),
                    'neto' : djelatnik.tip_racuna.placa_mjesecno()
                }
                kwargs.update({
                    'bruto' : kwargs['neto'] * 1.25
                })
                

                try:
                    Placa.objects.get(djelatnik=djelatnik, datum=kwargs.get('datum'))
                except Placa.DoesNotExist:
                    Placa.objects.create(djelatnik=djelatnik, **kwargs)

    @staticmethod
    def create_one(djelatnik):
        now = timezone.now()
        range_start = 0
        
        time_since = now - djelatnik.created_at
        months_since = int(time_since.days / 30)
        if now.day < 15:
            range_start = 1
        month = now.month
        year = now.year
        for i in range(range_start, months_since):
            if i % 12 == now.month:
                month = 12
                year -= 1
            else:
                month -= (i % 12)

            kwargs = {
                'datum' : datetime(year, month, 15, 0, 0, tzinfo=pytz.UTC),
                'naziv' : "{} - {}".format(i + 1, djelatnik.get_full_name()),
                'neto' : djelatnik.tip_racuna.placa_mjesecno()
            }
            kwargs.update({
                'bruto' : kwargs['neto'] * 1.25
            })
            

            try:
                Placa.objects.get(djelatnik=djelatnik, datum=kwargs.get('datum'))
            except Placa.DoesNotExist:
                Placa.objects.create(djelatnik=djelatnik, **kwargs)



    def __str__(self):
        return self.naziv
