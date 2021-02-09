from django.db import models
from django.urls import reverse
from djeca.models import Dijete


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
    smjena  = models.ForeignKey("smjene.Smjena", verbose_name="Smjena", null=True, blank=False, on_delete=models.CASCADE) # TODO: remove null

    created_at = models.DateTimeField("Datum stvaranja", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Datum ažuriranja", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Upis"
        verbose_name_plural = "Upisi"
    
    def get_related_dijete(self):
        ime = self.dijete_puno_ime.split(" ")[0],
        prezime = self.dijete_puno_ime.split(" ")[1]

        try:
            return Dijete.objects.get(ime=ime, prezime=prezime, datum_rodjenja=self.dijete_datum_rodjenja)
        except Dijete.DoesNotExist:
            return Dijete()

    def __str__(self):
        return "Zahtjev za upis: " + self.roditelj_puno_ime

    def get_absolute_url(self):
        return reverse("upisi:prikaz", kwargs={"pk": self.pk})
