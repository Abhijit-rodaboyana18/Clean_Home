from django.core.validators import RegexValidator
from django.db import models
home_choices = (
    ('1BHK','1BHK'),
    ('2BHK','2BHK'),
    ('Above 3BHK','Above 3BHK'),
    ('Garden','Garden'),
    ('Villa/Bunglow','Villa/Bunglow'),
    ('Office','Office')
)

staff_required = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5')

)

PHONE_REGEX = RegexValidator(r'^\+?1?\d{9,10}$',"Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")

# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15,validators=[PHONE_REGEX])
    email = models.EmailField()

    def __str__(self):
        return self.name

class Bookings(models.Model):
    user =  models.ForeignKey(Signup, on_delete=models.CASCADE)
    type_of_home = models.CharField(max_length=20, choices=home_choices)
    persons = models.CharField(max_length=20, choices=staff_required)
    address = models.TextField()
    zip_code = models.CharField(max_length=6)

    def __str__(self):
        return self.user.name