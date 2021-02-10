from django.db import models
from django.urls import reverse
from django.utils import timesince


class Dijete(models.Model):

    # Atributi
    ime            = models.CharField("Ime", max_length=64)
    prezime        = models.CharField("Prezime", max_length=64)
    datum_rodjenja = models.DateField("Datum rođenja")
    dodatne_informacije = models.TextField("Dodatne informacije") 

    # Vanjski ključevi
    roditelj        = models.ForeignKey("racuni.Racun", verbose_name="Roditelj", on_delete=models.CASCADE)
    program         = models.ForeignKey("programi.Program", verbose_name="Upisani program", null=True, on_delete=models.CASCADE)
    smjena          = models.ForeignKey("smjene.Smjena", verbose_name="Smjena čuvanja", blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Dijete"
        verbose_name_plural = "Djeca"

    @property
    def godine(self):
        return timesince.timesince(self.datum_rodjenja)

    def ceka_suglasnost(self):
        return self.suglasnost_set.filter(odobren__isnull=True).count() != 0

    def get_full_name(self):
        string = "{} {}".format(self.ime, self.prezime)
        return string.strip()
    
    def get_absolute_url(self):
        return reverse("djeca:prikaz", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.get_full_name()


class DobnaSkupina(models.Model):

    naziv       = models.CharField("Naziv", max_length=128)
    godine_min = models.FloatField("Donja granica - godine", help_text="Minimalna dob dijeteta u godinama")
    godine_max = models.FloatField("Gornja granica - godine", help_text="Maksimalna dob dijeteta u godinama")

    class Meta:
        verbose_name = "Dobna skupina"
        verbose_name_plural = "Dobne skupine"

    def __str__(self):
        return self.naziv