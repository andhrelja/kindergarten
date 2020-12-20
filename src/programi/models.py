from django.db import models
from django.urls import reverse
from vrtic.models import Vrtic

VRTIC = Vrtic.objects.get(id=1)
VRSTE_PROGRAMA = (
    ("Redoviti programi", 2400, VRTIC),
    ("Obogaćeni programi", 2600, VRTIC),
    ("Posebni programi", 2800, VRTIC),
    ("Kraći programi", 1800, VRTIC),
    ("Predškolski", 2400, VRTIC),
)

class VrstaPrograma(models.Model):

    # Atributi
    naziv           = models.CharField("Naziv programa", max_length=128)
    clanstvo_cijena = models.FloatField(
        "Cijena", help_text="Cijena mjesečne članarine")

    # Vanjski ključevi
    vrtic           = models.ForeignKey(
        "vrtic.Vrtic", verbose_name="Vrtić", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Vrsta programa"
        verbose_name_plural = "Vrste programa"
    

    def create(self):
        for vrsta_programa in VRSTE_PROGRAMA:
            defaults = {
                'naziv': vrsta_programa[0],
                'clanstvo_cijena': vrsta_programa[1],
                'vrtic': vrsta_programa[2],
            }
            VrstaPrograma.objects.get_or_create(**defaults)

    def __str__(self):
        return self.naziv

    def get_absolute_url(self):
        return reverse("programi:vrsta-detail", kwargs={"pk": self.pk})


class Program(models.Model):

    # Atributi
    naziv           = models.CharField("Naziv programa", max_length=128)
    dodatni_boravak = models.BooleanField("Dostupnost dodatnog boravka")

    # Vanjski ključevi
    vrsta_programa  = models.ForeignKey(
        "programi.VrstaPrograma", verbose_name="Vrsta programa", on_delete=models.CASCADE)
    radna_vremena   = models.ManyToManyField(
        "programi.RadnoVrijeme", verbose_name="Radna vremena")

    class Meta:
        verbose_name = "Program"
        verbose_name_plural = "Programi"

    def __str__(self):
        return self.naziv


class TipPrograma(models.Model):

    # Atributi
    naziv           = models.CharField("Naziv tipa programa", max_length=128)
    broj_sati       = models.IntegerField("Broj sati", help_text="")
    max_broj_djece  = models.IntegerField("Maksimalni broj djece")

    # Vanjski ključevi
    program         = models.ForeignKey(
        "programi.Program", verbose_name="Program", on_delete=models.CASCADE)
    dogadjaji       = models.ManyToManyField(
        "dogadjaji.Dogadjaj", verbose_name="Događaji")
    dobne_skupine   = models.ManyToManyField(
        "djeca.DobnaSkupina", verbose_name="Dobne skupine")

    class Meta:
        verbose_name = "Tip programa"
        verbose_name_plural = "Tipovi programa"

    def __str__(self):
        return self.naziv


class RadnoVrijeme(models.Model):

    # Atributi
    naziv_smjene    = models.CharField("Naziv smjene", max_length=64)
    vrijeme_start   = models.TimeField(
        "Vrijeme početka", auto_now=False, auto_now_add=False)
    vrijeme_kraj    = models.TimeField(
        "Vrijeme kraja", auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Radno vrijeme"
        verbose_name_plural = "Radna vremena"

    def __str__(self):
        naziv = "{}: {} - {}".format(self.naziv_smjene, self.vrijeme_start, self.vrijeme_kraj)
        return naziv.strip()
