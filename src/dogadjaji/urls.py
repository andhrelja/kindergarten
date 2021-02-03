from django.urls import path, include
from . import views

app_name = 'dogadjaji'
urlpatterns = [
    path("",                  views.DogadjajListView.as_view(), name="popis"),
    path("stvori/",           views.DogadjajCreateView.as_view(), name="stvori"),
    path("uredi/<int:pk>/",   views.DogadjajUpdateView.as_view(), name="uredi"),
    path("prikaz/<int:pk>/",  views.DogadjajDetailView.as_view(), name="prikaz"),
    path("izbrisi/<int:pk>/", views.DogadjajDeleteView.as_view(), name="izbrisi"),

    path("suglasnosti/<int:dogadjaj_pk>/", include("dogadjaji.suglasnosti.urls"))
]
