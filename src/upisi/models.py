from django.db import models
from django.urls import reverse


class Upis(models.Model):

    roditelj_puno_ime       = models.CharField("Ime i prezime", max_length=128)
    roditelj_email          = models.EmailField("Email adresa", max_length=254, help_text="Ovaj će se email koristiti za prijavu")
    roditelj_datum_rodjenja = models.DateField("Datum rođenja", auto_now=False, auto_now_add=False)
    roditelj_telefon        = models.CharField("Telefon", max_length=50)

    dijete_puno_ime         = models.CharField("Ime i prezime", max_length=128)
    dijete_datum_rodjenja   = models.DateField("Datum rođenja")
    dijete_dodatne_informacije = models.TextField("Dodatne informacije", null=True, blank=True)

    odobren      = models.BooleanField("Zahtjev odobren", default=None, null=True)
    obrazlozenje = models.TextField("Obrazloženje zahtjeva", blank=True)

    program = models.ForeignKey("programi.Program", verbose_name="Program", on_delete=models.CASCADE)

    created_at = models.DateTimeField("Datum stvaranja", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Datum ažuriranja", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Upis"
        verbose_name_plural = "Upisi"

    def __str__(self):
        return "Zahtjev za upis: " + self.roditelj_puno_ime

    def get_absolute_url(self):
        return reverse("upisi:prikaz", kwargs={"pk": self.pk})
