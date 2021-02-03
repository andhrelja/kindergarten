from django.urls import path
from . import views

app_name = 'racuni'
urlpatterns = [
    path('',                 views.RacunListView.as_view(), name="popis"),
    path('djelatnik/',       views.DjelatnikCreateView.as_view(), name="djelatnik-stvori"),    
    path('roditelj/',        views.RoditeljCreateView.as_view(), name="roditelj-stvori"),
    path('djelatnik/uredi/<int:pk>/', views.DjelatnikUpdateView.as_view(), name="djelatnik-uredi"),    
    path('roditelj/uredi/<int:pk>/',  views.RoditeljUpdateView.as_view(), name="roditelj-uredi"),
    path('prikaz/<int:pk>',  views.RacunDetailView.as_view(), name="prikaz"),
    path('izbrisi/<int:pk>', views.RacunDeleteView.as_view(), name="izbrisi"),

    path('prijava/', views.LoginView.as_view(), name="prijava"),
    path('odjava/',  views.LogoutView.as_view(), name="odjava"),    
]
