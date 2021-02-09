from django.db import models
from django.urls import reverse
from .suglasnosti.models import Suglasnost


# TODO: dodati suglasnost na prikazu događaja

class Dogadjaj(models.Model):

    # Atributi
    naziv           = models.CharField("Naziv", max_length=50)
    opis            = models.TextField("Opis događaja")
    adresa          = models.CharField(
        "Lokacija događaja", max_length=255)
    
    # Datum i vrijeme
    datum_start     = models.DateField(
        "Datum početka", auto_now=False, auto_now_add=False)
    datum_kraj      = models.DateField(
        "Datum završetka", auto_now=False, auto_now_add=False)
    vrijeme_start   = models.TimeField(
        "Vrijeme početka", auto_now=False, auto_now_add=False)
    vrijeme_kraj    = models.TimeField(
        "Vrijeme završetka", auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Događaj"
        verbose_name_plural = "Događaji"
    
    def inform_parents(self):
        message = ("<h2>Poštovani {roditelj},</h2>" 
            "<p>Ovim putem Vas obavještavamo da je vaše dijete {dijete} "
            "zabilježeno kao sudionik događaja {dogadjaj} u sklopu programa \"{program}\".</p>"
            "<p>Molimo Vas da potvrdite sudjelovanje djeteta koristeći obrazac na slijedećem "
            "<a href=\"https://kindergarenn.herokuapp.com/djeca/prikaz/{dijete_id}\">linku</a>.</p>"
            "<br><p>Srdačan pozdrav,<br>Kindergarten</p>"
        )

        for vp in self.vrstaprograma_set.all():
            for program in vp.program_set.all():
                for dijete in program.dijete_set.all():
                    dijete.roditelj.send_event_email("Kindergarten - " + self.naziv,
                        message.format(**dict(
                            roditelj=dijete.roditelj.get_full_name(), 
                            dijete=dijete, 
                            dogadjaj=self.naziv, 
                            program=program, 
                            dijete_id=dijete.id
                        )))
    

    def inform_parent(self, dijete):
        message = ("<h2>Poštovani {roditelj},</h2>" 
            "<p>Ovim putem Vas obavještavamo da je vaše dijete {dijete} "
            "zabilježeno kao sudionik događaja {dogadjaj} u sklopu programa \"{program}\".</p>"
            "<p>Molimo Vas da potvrdite sudjelovanje djeteta koristeći obrazac na slijedećem "
            "<a href=\"https://kindergarenn.herokuapp.com/djeca/prikaz/{dijete_id}\">linku</a>.</p>"
            "<br><p>Srdačan pozdrav,<br>Kindergarten</p>"
        )

        dijete.roditelj.send_event_email("Kindergarten - " + self.naziv,
            message.format(**dict(
                roditelj=dijete.roditelj.get_full_name(), 
                dijete=dijete.get_full_name(), 
                dogadjaj=self.naziv, 
                program=dijete.program, 
                dijete_id=dijete.id
            )))


    def create_consents(self):
        for vp in self.vrstaprograma_set.all():
            for program in vp.program_set.all():
                for dijete in program.dijete_set.all():
                    Suglasnost.objects.get_or_create(dogadjaj=self, dijete=dijete)
    
    def create_consent(self, dijete):
        Suglasnost.objects.get_or_create(dogadjaj=self, dijete=dijete)


    def __str__(self):
        return self.naziv

    def get_absolute_url(self):
        return reverse("dogadjaji:prikaz", kwargs={"pk": self.pk})
