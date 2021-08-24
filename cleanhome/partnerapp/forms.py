from django import forms
from.models import Partners


class Partner_form(forms.ModelForm):

    class Meta:
        model = Partners
        fields = '__all__'
