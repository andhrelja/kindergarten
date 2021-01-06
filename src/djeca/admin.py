from django.contrib import admin
from .models import (
    Dijete,
    DobnaSkupina
)

from .napredak.models import DijeteNapredak

admin.site.register(Dijete)
admin.site.register(DobnaSkupina)

admin.site.register(DijeteNapredak)
