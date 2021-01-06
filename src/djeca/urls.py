from django.urls import path, include
from . import views

app_name = 'djeca'
urlpatterns = [
    path('',                views.DijeteListView.as_view(), name="popis"),
    path('prikaz/<int:pk>', views.DijeteDetailView.as_view(), name="prikaz"),

    path('napredak/', include('djeca.napredak.urls')),
]
