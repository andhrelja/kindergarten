from django.db import models

# Create your models here.
class Djelatnik(models.Model):

    # Atributi
    telefon         = models.CharField("Kontakt telefon", max_length=16)

    # Vanjski ključevi
    user            = models.OneToOneField(
        "auth.User", verbose_name="Django korisnik", on_delete=models.CASCADE)
    tip_djelatnika  = models.ForeignKey(
        "racuni.TipDjelatnika", verbose_name="Tip djelatnika", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Djelatnik"
        verbose_name_plural = "Djelatnici"

    def __str__(self):
        return self.user.get_full_name()

class Roditelj(models.Model):

    # Atributi
    telefon = models.CharField("Kontakt telefon", max_length=16)
    skrbnik = models.BooleanField("Skrbnik")

    # Vanjski ključevi
    user = models.OneToOneField(
        "auth.User", verbose_name="Django korisnik", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Roditelj"
        verbose_name_plural = "Roditelji"

    def __str__(self):
        return self.user.get_full_name()


class TipDjelatnika(models.Model):

    # Atributi
    naziv       = models.CharField("Naziv tipa djelatnika", max_length=50)
    strucni_tim = models.BooleanField("Pripada stručnom timu", default=True)
    voditelj    = models.BooleanField("Voditelj je", default=False)

    # Vanjski ključevi
    tip_programa    = models.ForeignKey(
        "programi.TipPrograma", verbose_name="Tip programa", on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Tip djelatnika"
        verbose_name_plural = "Tipovi djelatnika"

    def __str__(self):
        return self.naziv

