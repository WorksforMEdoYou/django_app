from django.urls import path, re_path
from . import views

urlpatterns = [
    path('signup/',views.Signuppage, name='Signup'),
    path('Login/', views.Signin, name = "Signin"),
    path('Logout/',views.Logoutuser,name="Logout"),
    path('Details/', views.Datatable, name='DataTable'),   
]