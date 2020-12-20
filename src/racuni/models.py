from django.db import models
from django.urls import reverse
from .managers import CustomUserManager

# Create your models here.
class Racun(models.Model):

    # Atributi
    telefon         = models.CharField("Kontakt telefon", max_length=16)
    datum_rodjenja  = models.DateField("Datum rođenja", auto_now=False, auto_now_add=False)
    tip_racuna      = models.ForeignKey("racuni.TipRacuna", verbose_name="Tip računa", on_delete=models.CASCADE)

    # Vanjski ključevi
    user = models.OneToOneField("auth.User", verbose_name="Django korisnik", on_delete=models.CASCADE)
    objects = CustomUserManager()

    class Meta:
        verbose_name = "Račun"
        verbose_name_plural = "Računi"

    def __str__(self):
        string = "{} - {}".format(self.user.get_full_name(), self.tip_racuna.naziv)
        return string.strip()

    def get_absolute_url(self):
        return reverse("racuni:pregled", kwargs={"pk": self.pk})


class TipRacuna(models.Model):

    # Atributi
    naziv           = models.CharField("Naziv tipa", max_length=32)

    je_roditelj     = models.BooleanField("Roditelj")
    je_djelatnik    = models.BooleanField("Djelatnik")
    je_voditelj     = models.BooleanField("Voditelj", default=False)
    je_strucni_tim  = models.BooleanField("Pripada stručnom timu", default=False)
    
    # Vanjski ključevi
    tip_programa    = models.ForeignKey(
        "programi.TipPrograma", verbose_name="Tip programa", on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = "Djelatnik"
        verbose_name_plural = "Djelatnici"

    def __str__(self):
        return self.naziv
