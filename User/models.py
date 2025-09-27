from django.db import models

# Create your models here.
class UserDetails(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=100)
    user_address = models.CharField(max_length=100)
    user_gender = models.CharField(max_length=100)
    user_dob = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user_name}"