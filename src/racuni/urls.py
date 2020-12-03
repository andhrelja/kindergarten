from django.urls import path
from . import views

app_name = 'racuni'
urlpatterns = [
    path('prijava/', views.LoginView.as_view(), name="prijava"),
    path('odjava/', views.LogoutView.as_view(), name="odjava"),
    
]
