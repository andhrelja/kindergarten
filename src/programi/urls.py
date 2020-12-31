from django.urls import path
from . import views

app_name = 'programi'
urlpatterns = [
    path('vrste/',             
        views.VrstaProgramaListView.as_view(), name="popis-vrsta-programa"),
    
    path('vrsta/<int:vrsta_programa_id>/prikaz/', 
        views.ProgramListView.as_view(), name="popis-programa"),

    # JSON endpoints
    path('vrsta-programa/<int:vrsta_programa_id>/api', 
        views.VrstaProgramaJSONView.as_view(), name="vrsta-programa-json"),
    path('vrsta/<int:vrsta_programa_id>/api', 
        views.ProgramiJSONView.as_view(), name="programi-json"),
    path('<int:program_id>/dobne-skupine/api', 
        views.ProgramDobneSkupineJSONView.as_view(), name="program-dobne-skupine-json"),
    path('<int:program_id>/smjene/api', 
        views.ProgramSmjeneJSONView.as_view(), name="program-smjene-json"),
]
