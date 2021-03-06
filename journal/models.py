from datetime import date
from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
from workout.models import Approach, Workout, WorkoutSet

class Journal(models.Model):
    """
    Model for journal/calendar. 
    """
    workout_id = models.ForeignKey(Workout, on_delete=models.SET_NULL, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_date = models.DateField()
    # !!change name to workout_status!!
    status = models.IntegerField(default=0) # = [0="not started",1="started",2="complete"]
    checkin_status = models.IntegerField(default=0) # = [0="no",1="yes"]
    workout_status = models.IntegerField(default=0) # = [0="N/A", 1="not started",2="complete"]
    comments = models.TextField(max_length=200, null=True, blank=True)

    # Metadata
    class Meta:
        ordering = ['-entry_date']

    def json_res(self):
        """json response used in journal.py view for calendar.js"""
        return {
            'workout': self.workout_id.name,
            'status': self.status,
            'year': int(self.entry_date.strftime("%Y")),
            'month': int(self.entry_date.strftime("%m")),
            'day': int(self.entry_date.strftime("%d")),
            'journal': self.id
        }

    def __str__(self):
        """String for representing the Model object."""
        return str(self.entry_date) + ' - ' + self.user_id.username

    @property
    def is_today(self):
        return date.today() == self.entry_date

    def get_absolute_url(self):
        return reverse('journal:index')


class Note(models.Model):
    """Model representing notes/comments."""
    subject = models.CharField(max_length=30)
    comments = models.TextField(null=True, blank=True)
    tag = models.TextField(null=True, blank=True)
    journal_id = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        """String for representing the Model object."""
        return str(self.journal_id) + ' - ' + self.subject

    # def get_absolute_url(self):
    #     """Returns the url to access a detail record for this note."""
    #     return reverse('journal:detail', args=[str(self.id)])


class Checkin(models.Model):
    """ Model for User Check-in form"""
    journal_id = models.ForeignKey(Journal, on_delete=models.CASCADE, null=True)
    goal = models.CharField(max_length=1024, null=True, blank=True, help_text='Your goal or aim in a few words')
    weight = models.DecimalField(max_digits=5, decimal_places=2, help_text='Weight in KG', blank=True, null=True)
    chest = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    waist = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    upperarm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    forearm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    neck = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    upperleg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    calf = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return str(self.journal_id)


class Progress(models.Model):
    """Model for User progress"""
    workoutset = models.ForeignKey(WorkoutSet, on_delete=models.SET_NULL, null=True, related_name='progress')
    journal_id = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name='progress')
    reps = models.IntegerField(blank=True, null=True)
    weight = models.DecimalField(blank=True, null=True, decimal_places=1, max_digits=5)
    rpe = models.IntegerField(blank=True, null=True)  # = [difficulty from 0-10]
    approach_id = models.ForeignKey(Approach, on_delete=models.SET_NULL, null=True, blank=True, related_name='progress')
    alternative_exercise = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return str(self.id)

    def get_absolute_url(self):
        return reverse('journal:workout-view', kwargs={'pk': self.workoutset.workout_id, 'journal_id': self.journal_id.id})