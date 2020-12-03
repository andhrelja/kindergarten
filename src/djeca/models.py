from django.db import models


class Dijete(models.Model):

    # Atributi
    ime            = models.CharField("Ime", max_length=64)
    prezime        = models.CharField("Prezime", max_length=64)
    datum_rodjenja = models.IntegerField("Datum rođenja")
    dodatne_informacije = models.TextField("Dodatne informacije") 

    # Vanjski ključevi
    roditelj        = models.ForeignKey("racuni.Roditelj", verbose_name="Roditelj", on_delete=models.CASCADE)
    tip_programa    = models.ForeignKey("programi.TipPrograma", verbose_name="Program", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Dijete"
        verbose_name_plural = "Djeca"

    def get_full_name(self):
        string = "{} {}".format(self.ime, self.prezime)
        return string.strip()

    def __str__(self):
        return self.get_full_name()


class DijeteNapredak(models.Model):
    OCJENE = (
        (1, "Nedovoljan"),
        (2, "Dovoljan"),
        (3, "Dobar"),
        (4, "Vrlo dobar"),
        (5, "Odličan"),
    )

    # Atributi
    komentar    = models.TextField("Komentar")
    datum_start = models.DateField(
        "Datum početka praćenja", auto_now=False, auto_now_add=False)
    datum_kraj  = models.DateField(
        "Datum kraja praćenja", auto_now=False, auto_now_add=False)
    ocjena      = models.IntegerField(
        "Ocjena", choices=OCJENE, help_text="Ocjena djeteta u skali od 1 - 5")
    
    # Vanjski ključevi
    dijete      = models.ForeignKey("djeca.Dijete", verbose_name="Dijete", on_delete=models.CASCADE)
    djelatnik   = models.ForeignKey("racuni.Djelatnik", verbose_name="Djelatnik", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Dijete - napredak"
        verbose_name_plural = "Djeca - napretci"

    def __str__(self):
        naziv = "Napredak: {}".format(self.dijete.get_full_name())
        return naziv.strip()


class DobnaSkupina(models.Model):

    naziv      = models.CharField("Naziv", max_length=128)
    godine_min = models.IntegerField("Donja granica godina")
    godine_max = models.IntegerField("Gornja granica godina")

    class Meta:
        verbose_name = "Dobna skupina"
        verbose_name_plural = "Dobne skupine"

    def __str__(self):
        return self.naziv