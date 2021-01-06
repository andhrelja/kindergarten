from django.urls import path
from . import views

urlpatterns = [
    path('<int:dijete_pk>/novo/', views.NapredakCreateView.as_view(), name="stvori-napredak"),
]
