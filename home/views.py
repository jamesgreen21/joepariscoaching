from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages

from marketing.forms import EmailSubscribeForm
from workout.models import Routine, Workout, Approach

def index(request):
    form = EmailSubscribeForm()
    context = {
        'title': 'Home',
        'form': form,
    }
    return render(request, 'home/index.html', context)


class WorkoutListView(generic.ListView):
    model = Workout


class WorkoutDetailView(generic.DetailView):
    model = Workout