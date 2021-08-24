from django.contrib import admin
from .models import Partners


# Register your models here.

admin.site.register(Partners)

list_display = ['Name','Aadhaar','Email','Mobile','Profession','Experience','Salary']