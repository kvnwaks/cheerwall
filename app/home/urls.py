from django.urls import path

# from django.views.generic.base import RedirectView
from . import views

app_name = "home"

urlpatterns = [
    # path("", RedirectView.as_view(url="/admin", permanent=False), name="root-redirect"),
    path("", views.index, name="index")
]
