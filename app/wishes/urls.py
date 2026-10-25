"""Routes for the wishes app."""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.carousel, name="carousel"),
    path("add/", views.add, name="add"),
    path("thanks/", views.thanks, name="thanks"),
]
