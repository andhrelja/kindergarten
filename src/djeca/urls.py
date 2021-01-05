from django.urls import path
from . import views

app_name = 'djeca'
urlpatterns = [
    # path('djelatnik/', views.DjelatnikCreateView.as_view(), name="stvori-djelatnik"),    
    # path('roditelj/', views.RoditeljCreateView.as_view(), name="stvori-roditelj"),
    path('prikaz/<int:pk>', views.DijeteDetailView.as_view(), name="prikaz"),
    path('',        views.DijeteListView.as_view(), name="popis"),
]
