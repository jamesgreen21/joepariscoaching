import json
import datetime

from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from crispy_forms.helper import FormHelper

from journal.models import Journal, Note, Checkin, Progress
from workout.models import Workout, WorkoutSet
from journal.forms import CheckinForm


@login_required
def checkin(request):
    """
    Returns a view that renders the checkin page and form
    """
    if request.method == 'POST':
        # Check if journal entry exists
        journal = Journal.objects.filter(entry_date=timezone.now().date(),user_id=request.user.id)
        if not journal:
            journal = Journal(entry_date=timezone.now().date(),user_id=request.user,checkin_status=1)
            journal.save()
            journal = Journal.objects.filter(entry_date=timezone.now().date(),user_id=request.user.id)
        # !! Code needed to set checkin_status=1 if journal exists !!
        form = CheckinForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.journal_id = journal[0]
            obj.save()
            # messages.success(request, 'Check-in complete nice work!')
            return redirect('accounts:profile')

    else:
        # Add instance for edit checkin
        form = CheckinForm()

    context = {
        'title': 'Profile',
        'form': form,
        # 'subscribe_form': subscribe_form,
    }

    return render(request, 'checkin.html', context)


class JournalListView(ListView):

    template_name = 'journal_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Journal.objects.filter(user_id=self.request.user).exclude(entry_date__lt=datetime.datetime.today()).order_by('entry_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['journal_history'] = Journal.objects.filter(user_id=self.request.user).exclude(entry_date__gte=datetime.datetime.today()).order_by('entry_date')
        context['title'] = 'Journal'
        return context


class JournalDetailView(DetailView):

    model = Journal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Journal'
        return context


class JournalUpdateView(SuccessMessageMixin, UpdateView):
    model = Journal
    fields = ['workout_id']
    success_message = "Your Journal was successfully updated!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Journal'
        context['journal_id'] = self.kwargs['pk']
        return context


class WorkoutCompleteView(SuccessMessageMixin, UpdateView):
    model = Journal
    fields = ['comments']
    success_message = "Workout complete, well done!"
    template_name = 'workout/workout_complete_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Journal'
        context['journal_id'] = self.kwargs['pk']
        context['workout_id'] = self.kwargs['workout_id']
        return context

    def form_valid(self, form):
        form.instance.workout_status = 2
        return super(WorkoutCompleteView, self).form_valid(form)


class WorkoutDetailView(DetailView):

    model = Workout

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        progress = Progress.objects.filter(journal_id=self.kwargs['journal_id']).order_by('workoutset__order')
        next_set = len([set.workoutset.id for set in progress]) if progress else 0
        context['progress'] = progress
        context['title'] = 'Workout'
        context['journal_id'] = self.kwargs['journal_id']
        context['workout_id'] = self.kwargs['pk']
        try:
            context['next_set'] = WorkoutSet.objects.filter(workout=self.kwargs['pk']).order_by('order')[next_set]            
        except:
            context['next_set'] = False
        return context


class ProgressCreateView(SuccessMessageMixin, CreateView):
    model = Progress
    fields = ['reps','weight','rpe','alternative_exercise']
    success_message = "Success! Get ready for the next set and keep your eye on the timer."

    def __init__(self, *args, **kwargs):
        super(ProgressCreateView, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    def form_valid(self, form):
        journal = get_object_or_404(Journal, pk=self.kwargs['journal_id'])
        form.instance.journal_id = journal
        workoutset = get_object_or_404(WorkoutSet, pk=self.kwargs['workoutset'])
        form.instance.workoutset = workoutset
        return super(ProgressCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['set'] = get_object_or_404(WorkoutSet, pk=self.kwargs['workoutset'])
        context['title'] = 'Workout'
        context['journal_id'] = self.kwargs['journal_id']
        context['workout_id'] = self.kwargs['workout_id']
        return context


class ProgressUpdateView(SuccessMessageMixin, UpdateView):
    model = Progress
    fields = ['reps','weight','rpe','alternative_exercise']
    success_message = "Set updated successfully!"

    def __init__(self, *args, **kwargs):
        super(ProgressUpdateView, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['set'] = get_object_or_404(WorkoutSet, pk=self.kwargs['workoutset'])
        context['title'] = 'Edit Set'
        context['journal_id'] = self.kwargs['journal_id']
        context['workout_id'] = self.kwargs['workout_id']
        return context