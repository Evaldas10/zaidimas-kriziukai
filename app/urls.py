from django.urls import path
from . import views

urlpatterns = [
    path("", views.zaidimo_langas, name="zaidimas"),
]
