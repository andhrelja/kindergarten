from django.urls import path, include
from . import views

app_name = 'djeca'
urlpatterns = [
    path('',                  views.DijeteListView.as_view(), name="popis"),
    path('prikaz/<int:pk>',   views.DijeteDetailView.as_view(), name="prikaz"),
    path('uredi/<int:pk>',    views.DijeteUpdateView.as_view(), name="uredi"),
    path('izbrisi/<int:pk>',  views.DijeteDeleteView.as_view(), name="izbrisi"),

    path('napredak/', include('djeca.napredak.urls')),
]
