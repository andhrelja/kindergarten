from django.db import models


class RacunClanarina(models.Model):

    # Atributi
    naziv  = models.CharField("Naziv dokumenta", max_length=128)
    datum  = models.DateTimeField("Datum dokumenta", auto_now=False, auto_now_add=True)
    iznos  = models.FloatField("Iznos")
    PDV    = models.FloatField("PDV (%)", default=25.0)
    ukupno = models.FloatField("Ukupno")

    # Vanjski ključevi
    dijete = models.ForeignKey("djeca.Dijete", verbose_name="Dijete", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Račun - članarina"
        verbose_name_plural = "Računi - članarine"

    def __str__(self):
        return self.naziv


class PlacaDjelatnik(models.Model):

    # Atributi
    naziv     = models.CharField("Naziv dokumenta", max_length=50)
    datum     = models.DateTimeField("Datum dokumenta", auto_now=False, auto_now_add=True)
    bruto     = models.FloatField("Bruto iznos plaće")
    neto      = models.FloatField("Neto iznos plaće")
    
    # Vanjski ključevi
    tip_djelatnika = models.ForeignKey("racuni.TipDjelatnika", verbose_name="Tip djelatnika", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Plaća - djelatnik"
        verbose_name_plural = "Plaće - djelatnici"

    def __str__(self):
        return self.naziv
