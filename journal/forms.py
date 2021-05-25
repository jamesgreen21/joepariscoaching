from django import forms
from django.contrib.auth.models import User
from journal.models import Checkin

class CheckinForm(forms.ModelForm):
    """
    Returns a form for User checkin
    !!! Add journal_id join and create Journal entry
    """
    class Meta:
        model = Checkin
        fields = [
            'goal',
            'weight',
            'chest',
            'waist',
            'upperarm',
            'forearm',
            'neck',
            'upperleg',
            'calf',
            'comments'
        ]

    def __init__(self, *args, **kwargs):
        super(CheckinForm, self).__init__(*args, **kwargs)
        self.fields['goal'].widget.attrs.update({'class' : 'form-control'})
        self.fields['weight'].widget.attrs.update({'class' : 'form-control'})
        self.fields['chest'].widget.attrs.update({'class' : 'form-control'})
        self.fields['waist'].widget.attrs.update({'class' : 'form-control'})
        self.fields['upperarm'].widget.attrs.update({'class' : 'form-control'})
        self.fields['forearm'].widget.attrs.update({'class' : 'form-control'})
        self.fields['neck'].widget.attrs.update({'class' : 'form-control'})
        self.fields['upperleg'].widget.attrs.update({'class' : 'form-control'})
        self.fields['calf'].widget.attrs.update({'class' : 'form-control'})
        self.fields['comments'].widget.attrs.update({'class' : 'form-control'})