from django.urls import path
from . import views

urlpatterns = [
    path('texttospeech', views.Texttospeech, name="product1"),
]