from django import forms
from.models import Login

class adminform(forms.ModelForm):

    class Meta():
        model = Login
        fields = ['username','password']
        widget={'password':forms.PasswordInput}
