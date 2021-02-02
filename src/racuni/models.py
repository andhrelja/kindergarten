from django.db import models
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from .managers import CustomUserManager


TIPOVI_RACUNA = (
    (1, "Roditelj", 0),
    (2, "Voditeljica", 60),
    (3, "Odgojateljica", 40),
    (4, "Stručna suradnica pedagoginja", 50),
    (5, "Stručna suradnica psihologinja", 50),
    (6, "Stručna suradnica rehabilitatorica", 50),
    (7, "Stručna suradnica psihologinja za djecu s teškoćama", 55),
    (8, "Zdravstvena voditeljica", 45),
)

class Racun(models.Model):

    # Atributi
    telefon         = models.CharField("Kontakt telefon", max_length=16)
    datum_rodjenja  = models.DateField("Datum rođenja", auto_now=False, auto_now_add=False)
    
    je_roditelj     = models.BooleanField("Roditelj")
    je_djelatnik    = models.BooleanField("Djelatnik")
    je_voditelj     = models.BooleanField("Voditelj", default=False)
    je_strucni_tim  = models.BooleanField("Pripada stručnom timu", default=False)

    # Vanjski ključevi
    user        = models.OneToOneField("auth.User", verbose_name="Django korisnik", on_delete=models.CASCADE)
    tip_racuna  = models.ForeignKey("racuni.TipRacuna", verbose_name="Uloga korisnika", on_delete=models.CASCADE)
    objects = CustomUserManager()

    class Meta:
        verbose_name = "Račun"
        verbose_name_plural = "Računi"

    def send_event_email(self, subject, html_message):
        print(subject, html_message)
        #send_mail(subject, message="", html_message=html_message, from_email=settings.EMAIL_HOST_USER, recipient_list=[self.user.email])

    def get_full_name(self):
        return self.user.get_full_name()

    def __str__(self):
        string = "{} - {}".format(self.user.get_full_name(), self.tip_racuna.naziv)
        return string.strip()

    def get_absolute_url(self):
        return reverse("racuni:prikaz", kwargs={"pk": self.pk})


class TipRacuna(models.Model):

    # Atributi
    naziv           = models.CharField("Naziv tipa", max_length=128)
    satnica         = models.FloatField("Satnica", default=0)
    

    class Meta:
        verbose_name = "Tip računa"
        verbose_name_plural = "Tipovi računa"

    def create(self):
        tipovi_all = TipRacuna.objects.all()
        tipovi_all.delete()

        for tip_racuna in TIPOVI_RACUNA:
            defaults = {
                'id': tip_racuna[0],
                'naziv': tip_racuna[1],
                'satnica': tip_racuna[2],
            }
            TipRacuna.objects.get_or_create(id=defaults.pop('id'), **defaults)

    def __str__(self):
        return self.naziv
