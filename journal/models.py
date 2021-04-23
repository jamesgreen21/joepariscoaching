from django.db import models
from django.urls import reverse
from django.utils import timezone

from django.contrib.auth.models import User
from workout.models import Workout

class Journal(models.Model):
    """Model for journal/calendar."""
    workout_id = models.ForeignKey(Workout, on_delete=models.SET_NULL, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_date = models.DateField(default=timezone.now())

    # Metadata
    class Meta:
        ordering = ['-entry_date']

    def __str__(self):
        """String for representing the Model object."""
        return str(self.entry_date)


class Note(models.Model):
    """Model representing notes/comments."""
    subject = models.CharField(max_length=30)
    comments = models.TextField(null=True, blank=True)
    tag = models.TextField(null=True, blank=True)
    journal_id = models.ForeignKey(Journal, on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object."""
        return self.subject

    # def get_absolute_url(self):
    #     """Returns the url to access a detail record for this note."""
    #     return reverse('journal:detail', args=[str(self.id)])
