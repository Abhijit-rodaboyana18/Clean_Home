from django.contrib import admin

# Register your models here.
from .models import Signup, Bookings

admin.site.register(Signup)

admin.site.register(Bookings)
