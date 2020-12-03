from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('vrtic.urls')),
    path('dogadjaji/', include('dogadjaji.urls')),
    path('financije/', include('financije.urls')),
    path('programi/', include('programi.urls')),
    path('racuni/', include('racuni.urls')),
    path('djeca/', include('djeca.urls')),

    # Admin site
    path('admin/', admin.site.urls),
]
