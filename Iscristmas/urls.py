from django.urls import path
from . import views

urlpatterns = [
    path('', views.Christmas, name='christmastoday'),
]