from django.urls import path
from . import views

app_name = 'programi'
urlpatterns = [
    path('<int:vrsta_programa_id>/', views.ProgramListView.as_view(), name="popis-programa"),
]
