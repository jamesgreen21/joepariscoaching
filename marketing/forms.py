from django import forms
from .models import Subscribtion


class EmailSubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribtion
        fields = ('email', )
