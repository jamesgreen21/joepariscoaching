from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages

from marketing.forms import EmailSubscribeForm


def index(request):
    form = EmailSubscribeForm()
    context = {
        'title': 'Home',
        'form': form,
    }
    return render(request, 'index.html', context)
