from django.db import models


class Clanarina(models.Model):

    # Atributi
    naziv  = models.CharField("Naziv dokumenta", max_length=128)
    datum  = models.DateTimeField("Datum dokumenta", auto_now=False, auto_now_add=True)
    iznos  = models.FloatField("Iznos")
    PDV    = models.FloatField("PDV")
    ukupno = models.FloatField("Ukupno")

    # Vanjski ključevi
    dijete = models.ForeignKey("djeca.Dijete", verbose_name="Dijete", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Članarina"
        verbose_name_plural = "Članarine"

    def __str__(self):
        return self.naziv


class Placa(models.Model):

    # Atributi
    naziv     = models.CharField("Naziv dokumenta", max_length=50)
    datum     = models.DateTimeField("Datum dokumenta", auto_now=False, auto_now_add=True)
    bruto     = models.FloatField("Bruto iznos plaće")
    neto      = models.FloatField("Neto iznos plaće")
    
    # Vanjski ključevi
    djelatnik = models.ForeignKey("racuni.Racun", verbose_name="Djelatnik", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Plaća"
        verbose_name_plural = "Plaće"

    def __str__(self):
        return self.naziv
