from django.urls import path

from .views import home

from . import views

urlpatterns = [
    path('', home, name='home'),
    path("", views.index, name="index"),
]