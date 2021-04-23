import datetime

from django import forms
from .models import Approach

class WorkoutAppForm(forms.ModelForm):
    """
    Returns a workout app form
    """
    reps_recorded = forms.IntegerField(
        required=False,
        help_text='Reps'        
    )

    class Meta:
        model = Approach
        fields = ['reps_recorded', 'weight_recorded']

    def __init__(self, *args, **kwargs):
        super(WorkoutAppForm, self).__init__(*args, **kwargs)
        self.fields['reps_recorded'].widget.attrs.update({'class' : 'form-control'})
        self.fields['weight_recorded'].widget.attrs.update({'class' : 'form-control'})