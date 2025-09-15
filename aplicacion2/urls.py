from django.urls import path
from . import views
urlpatterns = [
    path("vista1/", views.mirada1),
    path("vista2/", views.mirada2),
]