from django.urls import path
from . import views

app_name = "upisi"
urlpatterns = [
    path('', views.UpisListView.as_view(), name="popis"),
    path('novo/', views.UpisCreateView.as_view(), name="stvori"),
    path('prikaz/<int:pk>/', views.UpisDetailView.as_view(), name="prikaz"),
    path('uredi/<int:pk>/', views.UpisUpdateView.as_view(), name="uredi"),
]
