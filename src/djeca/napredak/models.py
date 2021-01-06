from django.db import models
from django.urls import reverse


class DijeteNapredak(models.Model):
    OCJENE = (
        (5, "Odličan"),
        (4, "Vrlo dobar"),
        (3, "Dobar"),
        (2, "Dovoljan"),
        (1, "Nedovoljan"),        
    )

    # Atributi
    komentar    = models.TextField("Komentar")
    datum_start = models.DateField(
        "Datum početka praćenja", auto_now=False, auto_now_add=False)
    datum_kraj  = models.DateField(
        "Datum kraja praćenja", auto_now=False, auto_now_add=False)
    ocjena      = models.IntegerField(
        "Ocjena", choices=OCJENE, help_text="Ocjena djeteta u provedenom razdoblju")
    
    # Vanjski ključevi
    dijete      = models.ForeignKey("djeca.Dijete", verbose_name="Dijete", on_delete=models.CASCADE)
    autor       = models.ForeignKey("auth.User", verbose_name="Autor", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Dijete - napredak"
        verbose_name_plural = "Djeca - napretci"

    def get_absolute_url(self):
        return reverse("djeca:prikaz", kwargs={"pk": self.dijete.pk})
    
    def __str__(self):
        naziv = "Napredak: {}".format(self.dijete.get_full_name())
        return naziv.strip()

