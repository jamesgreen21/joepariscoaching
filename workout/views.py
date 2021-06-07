from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.contrib.auth.decorators import login_required

from workout.models import Routine, Workout, Approach
from journal.models import Journal, Progress
from workout.forms import WorkoutAppForm


class WorkoutView(DetailView):

    model = Journal
    template_name = 'workout/index.html'

    def get_context_data(self, **kwargs):
        # pass journal_id and approach_id
        context = super(WorkoutView, self).get_context_data(**kwargs)
        progress = Progress.objects.filter(journal_id=self.kwargs['pk'])
        next_approach = len([item.approach_id.id for item in progress])
        context['next_workout'] = Workout.objects.filter(pk=self.object.workout_id.id).values('routines__approachs__id').order_by(
            'routines__order',
            'routines__approachs__set_number')[next_approach]
        return context

# class ProgressCreate(CreateView):

#     model = Progress
#     template_name = 'workout/progress_create.html'
#     fields = ['reps','weight','journal_id','approach_id']

#     def get_context_data(self, **kwargs):
#         context = super(ProgressCreate, self).get_context_data(**kwargs)
#         context['journal'] = get_object_or_404(Journal, pk=self.kwargs['journal_id'])
#         return context

#     def form_valid(self, form):
#         self.fields['reps'].widget.attrs.update({'class' : 'form-control form-control-lg'})
#         return super(ProgressCreate, self).form_valid(form)


@login_required
def progress_create(request, pk, approach_id):
    """
    Returns a view that renders the main Workout app and WorkoutAppForm form
    Note: pk=journal_id
    """
    journal = Journal.objects.filter(pk=pk, workout_id__routines__approachs__id=approach_id).values(
        'id',
        'entry_date',
        'workout_id__id',
        'workout_id__name',
        'workout_id__routines__exercise_id__name',
        'workout_id__routines__exercise_id__equipment_id__name',
        'workout_id__routines__approachs__perform_id__name',
        'workout_id__routines__approachs__id',
        'workout_id__routines__approachs__set_number',
        'workout_id__routines__approachs__reps_targetted',
    ).first()

    if request.method == 'POST':
        form = WorkoutAppForm(request.POST)
        if form.is_valid():
            form.save()
            progress = Progress.objects.filter(journal_id=pk)
            next_approach = len([item.approach_id.id for item in progress])
            try:
                approach_id = Workout.objects.filter(pk=journal['workout_id__id']).values('routines__approachs__id').order_by(
                    'routines__order',
                    'routines__approachs__set_number')[next_approach]['routines__approachs__id']
            except:
                return redirect('workout:complete', pk)
            return redirect('workout:create-progress', pk, approach_id)

    else:
        form = WorkoutAppForm()

    context = {
        'title': 'Workout',
        'journal': journal,
        'form': form,
    }
    return render(request, 'workout/progress_create.html', context)


def complete_workout(request, pk):
    """
    Complete the active workout and return to Journal
    """
    instance = get_object_or_404(Journal, pk=pk)
    instance.status = 2  # Workout "complete" status
    instance.save()
    # messages.success(request, 'Check-in complete nice work!')
    return redirect('journal:index')
 