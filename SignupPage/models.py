from django.db import models

#userdataSignup
class Usersignup(models.Model):
    Firstname = models.CharField(max_length=100)
    email = models.EmailField(max_length= 254)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    conformpassword = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Firstname