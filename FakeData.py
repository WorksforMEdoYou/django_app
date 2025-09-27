import os
os.environ.setdefault(key='DJANGO_SETTINGS_MODULE', value='GreensProject.settings')

import django
django.setup()

import faker
from random import randint
fake = faker.Faker()

from SignupPage.models import Usersignup

def generatefakedata():
    f_name, f_gender, f_age, f_email, f_password = fake.name(), fake.passport_gender(), randint(18,60), fake.email(True,"gmail.com"), fake.password
    Usersignup.objects.get_or_create(Firstname=f_name, email=f_email, age=f_age, gender=f_gender, password=f_password, conformpassword=f_password)

data = int(input("Users that you want= "))
for i in range(data):
    generatefakedata()
print("Done")