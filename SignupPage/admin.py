from django.contrib import admin
from .models import Usersignup

class UsersignupAdmin(admin.ModelAdmin):
    list_display = ('Firstname', 'email', 'age', 'gender')  # Specify fields to show in the list view

# Register the Usersignup model with the custom admin
admin.site.register(Usersignup, UsersignupAdmin)
