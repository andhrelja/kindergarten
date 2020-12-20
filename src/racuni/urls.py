from django.urls import path, include
from . import views

app_name = 'racuni'
urlpatterns = [
    path('upisi/', include('racuni.upisi.urls')),
    path('prijava/', views.LoginView.as_view(), name="prijava"),
    path('odjava/',  views.LogoutView.as_view(), name="odjava"),
    
    path('djelatnik/', views.DjelatnikCreateView.as_view(), name="stvori-djelatnik"),    
    path('roditelj/', views.RoditeljCreateView.as_view(), name="stvori-roditelj"),
    path('prikaz/<int:pk>', views.RacunDetailView.as_view(), name="prikaz"),
    path('',        views.RacunListView.as_view(), name="popis"),
]
