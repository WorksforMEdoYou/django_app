from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    empId = models.IntegerField()
    employeeName = models.CharField(max_length=50)
    password = models.CharField(max_length=8)
    designationModels = models.CharField(max_length=50)
    phno = models.IntegerField()
