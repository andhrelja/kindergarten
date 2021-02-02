from django.db import models
from django.urls import reverse

class Suglasnost(models.Model):

    dogadjaj = models.ForeignKey("dogadjaji.Dogadjaj", verbose_name="Dogadjaj", on_delete=models.CASCADE)
    dijete   = models.ForeignKey("djeca.Dijete", verbose_name="Dijete", on_delete=models.CASCADE)
    odobren  = models.BooleanField("Odobren", default=False, help_text="Označite dajete li suglasnost za prisustvo djeteta u predstavi")

    created_at = models.DateTimeField("Datum stvaranja", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Datum ažuriranja", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Suglasnost"
        verbose_name_plural = "Suglasnosti"
        unique_together = ['dijete', 'dogadjaj']

    def __str__(self):
        if self.odobren:
            return "{} - {} (odobren)".format(self.dijete, self.dogadjaj)
        else:
            return "{} - {} (nije odobren)".format(self.dijete, self.dogadjaj)

    def get_absolute_url(self):
        return reverse("dogadjaji:suglasnost-prikaz", kwargs={
            "dogadjaj_pk": self.dogadjaj.pk, 
            "suglasnost_pk": self.pk
        })
