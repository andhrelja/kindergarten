from django import template
from vrtic.models import Vrtic
from upisi.models import Upis

register = template.Library()


@register.filter
def vrste_programa(name):
    vrtic = Vrtic.objects.get(naziv=name)
    return vrtic.vrstaprograma_set.all()

@register.filter
def vrtic(name):
    return Vrtic.objects.get(naziv=name)

@register.filter
def vrtic_email(name):
    return Vrtic.objects.get(naziv=name).kontakt_email

@register.filter
def vrtic_adresa(name):
    return Vrtic.objects.get(naziv=name).adresa

@register.filter
def vrtic_broj(name):
    return Vrtic.objects.get(naziv=name).kontakt_broj

@register.filter
def upisi_na_cekanju(extra=None):
    return Upis.objects.filter(odobren__isnull=True).count()