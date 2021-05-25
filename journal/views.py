import json
import datetime

from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required

from journal.models import Journal, Note, Checkin
from journal.forms import CheckinForm


@login_required
def journal(request):
    """
    Returns a view that renders the Journal calendar page.
    Notes data last 60 Days only with history btn (parameter=note_cap).
    """
    journal = [i.json_res() for i in Journal.objects.filter(user_id=request.user.id).exclude(workout_id__isnull=True)]
    json_res = {"events": journal}
    journal_id = Journal.objects.filter(
        entry_date=timezone.now().date(),
        user_id=request.user.id
        ).values('id').first()

    note_cap = timezone.now() - datetime.timedelta(days=60)
    notes = Note.objects.filter(
        journal_id__user_id=request.user.id,
        journal_id__entry_date__gte=note_cap
        ).order_by('-journal_id__entry_date')
    context = {
        'title': 'Journal',
        'notes': notes,
        'journal': json_res,
        'journal_id': journal_id,
    }
    return render(request, 'journal.html', context)


@login_required
def checkin(request):
    """
    Returns a view that renders the checkin page and form
    """
    if request.method == 'POST':
        # Check if journal entry exists
        journal = Journal.objects.filter(entry_date=timezone.now().date(),user_id=request.user.id)
        if not journal:
            journal = Journal(entry_date=timezone.now().date(),user_id=request.user)
            journal.save()
            journal = Journal.objects.filter(entry_date=timezone.now().date(),user_id=request.user.id)
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
        'title': 'Check-in',
        'form': form,
        # 'subscribe_form': subscribe_form,
    }

    return render(request, 'checkin.html', context)