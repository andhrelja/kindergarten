from django.urls import path
from . import views

app_name = 'financije'
urlpatterns = [
    path("", views.ClanarinaListView.as_view(), name="popis"),
]
