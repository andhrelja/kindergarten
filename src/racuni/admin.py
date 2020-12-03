from django.contrib import admin
from .models import (
    Djelatnik,
    TipDjelatnika,
    Roditelj
)

admin.site.register(Djelatnik)
admin.site.register(TipDjelatnika)
admin.site.register(Roditelj)
