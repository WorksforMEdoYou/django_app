from django.urls import path
from . import views

urlpatterns = [
    path('',views.Homepage, name='Homepage'), 
    path('Newsletter/',views.Newsletter, name="Newsletter"), 
]