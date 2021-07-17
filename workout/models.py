from django.db import models
from django.urls import reverse


class Equipment(models.Model):
    """Model for exercises."""    
    name = models.CharField(max_length=50)

    # Metadata
    class Meta:
        ordering = ['-name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Exercise(models.Model):
    """Model representing a exercises."""
    ENDURANCE = 'EN'
    STRENGTH = 'ST'
    CORE = 'CO'
    FLEXIBILITY = 'FL'
    NOT_AVAILABLE = 'NA'
    EXERCISE_TYPES = [
        (STRENGTH, 'Strength'),
        (ENDURANCE, 'Endurance'),
        (CORE, 'Core'),
        (FLEXIBILITY, 'Flexibility'),
    ]
    name = models.CharField(max_length=50)
    tooltip = models.TextField(null=True, blank=True)
    bodypart = models.CharField(max_length=50,null=True, blank=True)
    exercise_type = models.CharField(
        max_length=2,
        choices=EXERCISE_TYPES,
        default=NOT_AVAILABLE,
    )
    tag = models.TextField(null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this exercise."""
        return reverse('exercise-detail', args=[str(self.id)])


class Workout(models.Model):
    """Model representing a Workouts."""
    name = models.CharField(max_length=50)
    tag = models.TextField(null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record."""
        return reverse('home:workouts-detail', args=[str(self.id)])


class Instructions(models.Model):
    title = models.CharField(max_length=20)
    detail = models.TextField()

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class WorkoutSet(models.Model):
    """Model for Workout Sets within the Workout."""
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='set')
    exercise = models.ForeignKey(Exercise, on_delete=models.SET_NULL, null=True)
    order = models.IntegerField(default=1)
    reps = models.IntegerField(default=0)
    instruction = models.ForeignKey(Instructions, on_delete=models.RESTRICT, null=True, blank=True)
    rpe = models.IntegerField(default=0)  # = [difficulty from 0-10]
    rest = models.IntegerField(null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.workout.name + ' - ' + self.exercise.name + ': ' + str(self.order)


# Remove code below this point
class Routine(models.Model):
    """Model for Routines."""
    workout_id = models.ForeignKey(Workout, on_delete=models.CASCADE, verbose_name='Workout', related_name='routines')
    exercise_id = models.ForeignKey(Exercise, on_delete=models.SET_NULL, null=True, verbose_name='Exercise')
    order = models.IntegerField(default=1)

    def __str__(self):
        """String for representing the Model object."""
        return self.workout_id.name + ' - ' + self.exercise_id.name


class Perform(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Approach(models.Model):
    """Model for Routines."""
    routine_id = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='approachs')
    set_number = models.IntegerField(default=1)
    reps_targetted = models.IntegerField(default=0, verbose_name='Reps')
    duration = models.DecimalField(max_digits=5, decimal_places=2, default=0, help_text='Time in Minutes')
    perform_id = models.ForeignKey(Perform, on_delete=models.RESTRICT, null=True, verbose_name='Perform')

    def __str__(self):
        """String for representing the Model object."""
        return str(self.routine_id) + ': Set ' + str(self.set_number)