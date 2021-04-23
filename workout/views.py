from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Max
from django.contrib.auth.decorators import login_required

from workout.models import Routine, Workout, Approach
from .forms import WorkoutAppForm

# def index(request):
#     """View function for home page of site."""

#     # Get main objects
#     # workouts = Workout.objects.all()

#     # context = {
#     #     'workouts': workouts,
#     # }

#     # Render the HTML template index.html with the data in the context variable
    # return render(request, 'workout/index.html')


class WorkoutListView(generic.ListView):
    model = Workout
    template_name = 'workout_list.html'


@login_required
def workout(request, pk):
    """
    Returns a view that renders the main Workout app and WorkoutAppForm form
    """
    routines = Routine.objects.filter(workout_id=pk).order_by('order')
    approaches = Approach.objects.filter(routine_id__in=[routine.id for routine in routines]).order_by('set_number')
    workout = get_object_or_404(Workout, pk=pk)
    active = Approach.objects.filter(
        routine_id__in=[routine.id for routine in routines],
        routine_id__complete=False,
        reps_recorded__isnull=True
    ).order_by('routine_id__order').first()

    context = {
        'title': 'Workout',
        'workout': workout,
        'routines': routines,
        'approaches': approaches,
        'active': active
    }
    return render(request, 'workout_detail.html', context)


def approach(request, pk, routine_id, approach_id):
    max_set = Approach.objects.filter(routine_id=routine_id).aggregate(Max('set_number')).get('set_number__max')
    instance = get_object_or_404(Approach, pk=approach_id)
    form = WorkoutAppForm(data=request.POST, instance=instance)
    if form.is_valid():
        form.save()
        if instance.set_number == max_set:
            """Switch Complete status to True on last set_number"""
            routine = Routine.objects.get(pk=instance.routine_id.id)
            routine.complete = True
            routine.save()

        return redirect('workout:detail', pk=pk)