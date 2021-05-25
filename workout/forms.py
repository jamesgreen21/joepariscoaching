import datetime

from django import forms
from journal.models import Progress

class WorkoutAppForm(forms.ModelForm):
    """
    Returns a workout app form
    """
    def __init__(self, *args, **kwargs):
        super(WorkoutAppForm, self).__init__(*args, **kwargs)
        self.fields['reps'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['weight'].widget.attrs.update({'class' : 'form-control form-control-lg'})

    class Meta:
        model = Progress
        fields = ['reps', 'weight', 'journal_id', 'approach_id']
