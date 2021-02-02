from django.urls import path
from . import views

urlpatterns = [
    path("", views.SuglasnostListView.as_view(), name="suglasnost-popis"),
    path("stvori/", views.SuglasnostCreateView.as_view(), name="suglasnost-stvori"),
    path("uredi/<int:suglasnost_pk>/", views.SuglasnostUpdateView.as_view(), name="suglasnost-uredi"),
    path("prikaz/<int:suglasnost_pk>/", views.SuglasnostDetailView.as_view(), name="suglasnost-prikaz"),
    path("izbrisi/<int:suglasnost_pk>/", views.SuglasnostDeleteView.as_view(), name="suglasnost-izbrisi")
]