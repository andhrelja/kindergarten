from django.urls import path
from . import views

app_name = 'vrtic'
urlpatterns = [
    path('', views.index, name="home"),
    path('o-nama/', views.about, name="o-nama")
]
