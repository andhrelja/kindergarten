from django.db import models
from django.urls import reverse



class VrstaPrograma(models.Model):

    # Atributi
    naziv           = models.CharField("Naziv programa", max_length=128)
    opis            = models.TextField("Opis vrste programa")
    clanstvo_cijena = models.FloatField(
        "Cijena", help_text="Cijena mjesečne članarine")

    # Vanjski ključevi
    vrtic           = models.ForeignKey(
        "vrtic.Vrtic", verbose_name="Vrtić", on_delete=models.CASCADE)
    dogadjaji       = models.ManyToManyField(
        "dogadjaji.Dogadjaj", verbose_name="Događaji", blank=True)

    class Meta:
        verbose_name = "Vrsta programa"
        verbose_name_plural = "Vrste programa"
    

    def __str__(self):
        return self.naziv

    def get_absolute_url(self):
        return reverse("programi:vrsta-detail", kwargs={"pk": self.pk})


class Program(models.Model):

    # Atributi
    naziv           = models.CharField("Naziv programa", max_length=128)
    dodatni_boravak = models.BooleanField("Dostupnost dodatnog boravka")
    max_broj_djece  = models.IntegerField("Maksimalni broj djece")
    opis            = models.TextField("Opis programa", default="")

    # Vanjski ključevi
    vrsta_programa  = models.ForeignKey(
        "programi.VrstaPrograma", verbose_name="Vrsta programa", on_delete=models.CASCADE)
    smjene          = models.ManyToManyField(
        "smjene.Smjena", verbose_name="Smjene")
    dobne_skupine   = models.ManyToManyField(
        "djeca.DobnaSkupina", verbose_name="Dobne skupine")

    class Meta:
        verbose_name = "Program"
        verbose_name_plural = "Programi"

    def __str__(self):
        return self.naziv
