from django import forms
from .models import UrlData

from django import forms

class Url(forms.ModelForm):

    class Meta :
        model = UrlData
        fields = ('url',)

