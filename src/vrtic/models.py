from django.db import models
from django.shortcuts import reverse


class Vrtic(models.Model):

    # Atributi
    naziv           = models.CharField("Naziv vrtića", max_length=128)
    adresa          = models.CharField("Adresa", max_length=128)
    kontakt_broj    = models.CharField("Kontakt broj", max_length=16)
    kontakt_email   = models.EmailField("Email kontakt", max_length=254)

    class Meta:
        verbose_name = "Vrtić"
        verbose_name_plural = "Vrtići"

    def __str__(self):
        return self.naziv

    def get_absolute_url(self):
        return reverse("vrtic:detail", kwargs={"pk": self.pk})
    