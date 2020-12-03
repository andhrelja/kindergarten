from django.db import models
from django.urls import reverse


class Dogadjaj(models.Model):

    # Atributi
    naziv           = models.CharField("Naziv", max_length=50)
    opis            = models.TextField("Opis događaja")
    adresa          = models.CharField(
        "Lokacija događaja", max_length=255)
    
    # Datum i vrijeme
    datum_start     = models.DateField(
        "Datum početka", auto_now=False, auto_now_add=False)
    datum_kraj      = models.DateField(
        "Datum kraja", auto_now=False, auto_now_add=False)
    vrijeme_start   = models.TimeField(
        "Vrijeme početka", auto_now=False, auto_now_add=False)
    vrijeme_kraj    = models.TimeField(
        "Vrijeme kraja", auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Događaj"
        verbose_name_plural = "Događaji"

    def __str__(self):
        return self.naziv

    def get_absolute_url(self):
        return reverse("dogadjaji:detail", kwargs={"pk": self.pk})
