from django.db import models


profession_choices = (
    ('Garden_cleaner','Garden_cleaner'),
    ('Electrician','Electrician'),
    ('Kitchen_cleaner','Kitchen_cleaner'),
    ('Painter','Painter'),
    ('Home_cleaner','Home_cleaner'),)

# Create your models here.
class Partners(models.Model):
    name = models.CharField(max_length=50)
    aadhaar = models.CharField(max_length=12, default="0")
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    profession  = models.CharField(max_length=20, choices=profession_choices)
    experience = models.IntegerField()
    salary = models.CharField(max_length=10)
