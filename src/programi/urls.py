from django.urls import path
from . import views

app_name = 'programi'
urlpatterns = [
    path('', views.VrstaProgramaListView.as_view(), name="popis-vrsta-programa"),
    path('prikaz/<int:vrsta_programa_id>/', views.ProgramListView.as_view(), name="popis-programa"),
]
