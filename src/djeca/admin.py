from django.contrib import admin
from .models import (
    Dijete,
    DijeteNapredak,
    DobnaSkupina
)

admin.site.register(Dijete)
admin.site.register(DijeteNapredak)
admin.site.register(DobnaSkupina)
