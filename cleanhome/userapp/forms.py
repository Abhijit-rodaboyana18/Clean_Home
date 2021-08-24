from django import forms
from.models import Signup
from.models import Bookings


class Signup_Form(forms.ModelForm):

    class Meta:
        model = Signup
        fields = ['name', 'mobile', 'email']

class Login_Form(forms.Form):

    mobile = forms.CharField(max_length=10)

class Bookings_Form(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ['user','type_of_home','persons','address','zip_code']


