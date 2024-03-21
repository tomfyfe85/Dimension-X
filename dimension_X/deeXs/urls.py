from django.urls import path
from . import views

urlpatterns = [path("", views.deeXs, name="deeXs")]
