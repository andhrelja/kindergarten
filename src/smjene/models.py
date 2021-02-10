from django.db import models
from django.urls import reverse

from datetime import datetime, date


class Smjena(models.Model):

    # Atributi
    naziv_smjene    = models.CharField("Naziv smjene", max_length=64)
    vrijeme_start   = models.TimeField(
        "Vrijeme početka", auto_now=False, auto_now_add=False)
    vrijeme_kraj    = models.TimeField(
        "Vrijeme kraja", auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Smjena"
        verbose_name_plural = "Smjene"


    def vrijeme_od_do(self):
        vrijeme_od = self.vrijeme_start.strftime("%H:%M")
        vrijeme_do = self.vrijeme_kraj.strftime("%H:%M")
        return "{} - {}".format(vrijeme_od, vrijeme_do)
    
    def broj_sati(self):
        start = datetime.combine(date.today(), self.vrijeme_start)
        kraj = datetime.combine(date.today(), self.vrijeme_kraj)
        tdelta = kraj - start
        return tdelta.seconds / 3600

    def __str__(self):
        naziv = "{}: {}".format(self.naziv_smjene, self.vrijeme_od_do())
        return naziv.strip()


class DjelatnikSmjenaProgram(models.Model):

    # Atributi
    djelatnik  = models.ForeignKey("racuni.Racun", verbose_name="Djelatnik", on_delete=models.CASCADE)
    smjena     = models.ForeignKey("smjene.Smjena", verbose_name="Smjena", on_delete=models.CASCADE)
    program    = models.ForeignKey("programi.Program", verbose_name="Program", on_delete=models.CASCADE)

    # Vanjski ključevi
    created_by = models.ForeignKey("auth.User", verbose_name="Autor", on_delete=models.CASCADE)
    created_at = models.DateTimeField("Vrijeme stvaranja", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Vrijeme ažuriranja", auto_now=True, auto_now_add=False)


    class Meta:
        verbose_name = "Djelatnik - smjena i program"
        verbose_name_plural = "Djelatnici - smjene i programi"
        unique_together = ['djelatnik', 'smjena']

    @property
    def satnica(self):
        pass

    def __str__(self):
        naziv = "{} - {}".format(self.djelatnik.get_full_name(), self.smjena.naziv_smjene)
        return naziv.strip()

    def get_absolute_url(self):
        return reverse("DjelatnikSmjenaProgram_detail", kwargs={"pk": self.pk})

        