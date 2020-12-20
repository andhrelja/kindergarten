from django.urls import path
from . import views

app_name = 'racuni'
urlpatterns = [
    path('prijava/', views.LoginView.as_view(), name="prijava"),
    path('odjava/',  views.LogoutView.as_view(), name="odjava"),
    
    path('djelatnik/', views.DjelatnikCreateView.as_view(), name="stvori-djelatnik"),    
    path('roditelj/', views.RoditeljCreateView.as_view(), name="stvori-roditelj"),    
    path('',        views.RacunListView.as_view(), name="popis"),
]
