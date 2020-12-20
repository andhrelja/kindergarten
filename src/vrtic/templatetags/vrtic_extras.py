from django import template
from vrtic.models import Vrtic

register = template.Library()


@register.filter
def vrste_programa(name):
    vrtic = Vrtic.objects.get(naziv=name)
    return vrtic.vrstaprograma_set.all()
