import json
import datetime
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required

from journal.models import Journal, Note


# class JournalListView(generic.ListView):
#     model = Journal
#     queryset = Journal.objects.all()
#     template_name = 'journal.html'

#     def get_context_data(self, **kwargs):
#         context = super(JournalListView, self).get_context_data(**kwargs)
#         context['notes'] = Note.objects.all()
#         context['title'] = 'Journal'
#         return context


@login_required
def journal(request):
    """
    Returns a view that renders the Journal calendar page.
    """
    notes = Note.objects.filter(journal_id__user_id=request.user.id).order_by('-journal_id__entry_date')
    journal = Journal.objects.filter(user_id=request.user.id).exclude(workout_id__isnull=True).values('id', 'workout_id', 'workout_id__name', 'entry_date')
    json_res = {"events":[]}

    for entry in journal:
        json_obj = dict(
            workout = entry['workout_id__name'],
            status = 'Complete',
            year=int(entry['entry_date'].strftime("%Y")),
            month=int(entry['entry_date'].strftime("%m")),
            day=int(entry['entry_date'].strftime("%d")),
        )
        json_res["events"].append(json_obj)

    context = {
        'title': 'Journal',
        'notes': notes,
        'journal': json_res
    }
    return render(request, 'journal.html', context)