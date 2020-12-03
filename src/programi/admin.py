from django.contrib import admin
from .models import (
    VrstaPrograma,
    Program,
    TipPrograma,
    RadnoVrijeme
)

admin.site.register(VrstaPrograma)
admin.site.register(Program)
admin.site.register(TipPrograma)
admin.site.register(RadnoVrijeme)