from django import template


register = template.Library()

@register.filter
def suglasnosti(dogadjaj, djeca):
    return dogadjaj.suglasnost_set.filter(dijete__in=djeca)