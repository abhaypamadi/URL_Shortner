from django import forms
from .models import Url

class UrlCreateForm(forms.ModelForm):
    class Meta:
        model = Url
        exclude = ['short_code']
