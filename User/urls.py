from django.urls import path
from . import views

urlpatterns = [
    path('AllData/', views.get_user, name='AllData'),
    path('NewData/', views.create_user, name='Create_User'),
    path('UpdateData/<pk:int>/', views.update_user, name='Update_User'),
    path('Delete/<pk:int>/', views.delete_user, name='DElete_user')
]