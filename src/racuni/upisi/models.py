from django.db import models
from django.urls import reverse


class Upis(models.Model):

    roditelj_puno_ime       = models.CharField("Ime i prezime", max_length=128)
    roditelj_email          = models.EmailField("Email adresa", max_length=254)
    roditelj_datum_rodjenja = models.DateField("Datum rođenja", auto_now=False, auto_now_add=False)
    roditelj_telefon        = models.CharField("Telefon", max_length=50)

    dijete_puno_ime         = models.CharField("Ime i prezime", max_length=128)
    dijete_datum_rodjenja   = models.DateField("Datum rođenja")

    odobren      = models.BooleanField("Zahtjev odobren", null=True)
    obrazlozenje = models.TextField("Obrazloženje zahtjeva", blank=True)

    created_at = models.DateTimeField("Datum stvaranja", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Datum ažuriranja", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Upis"
        verbose_name_plural = "Upisi"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("racuni:upisi-prikaz", kwargs={"pk": self.pk})
