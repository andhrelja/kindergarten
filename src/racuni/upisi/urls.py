from django.urls import path
from . import views

urlpatterns = [
    path('stvori/', views.UpisCreateView.as_view(), name="upisi-stvori"),
    path('prikaz/<int:pk>/', views.UpisDetailView.as_view(), name="upisi-prikaz"),

    path('uredi/<int:pk>/', views.UpisUpdateView.as_view(), name="upisi-uredi"),

    path('', views.UpisListView.as_view(), name="upisi-popis"),

]
