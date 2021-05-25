from django.contrib import admin
from .models import Journal, Note, Progress, Checkin

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_filter = ('subject', 'journal_id')


@admin.register(Journal)
class JournalBuilderAdmin(admin.ModelAdmin):
    fields = ['entry_date', 'user_id', 'workout_id','status']
    list_display  = ('pk','entry_date', 'user_id', 'workout_id','status')


@admin.register(Checkin)
class CheckinAdmin(admin.ModelAdmin):
    pass


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display  = ('pk','journal_id_id', 'approach_id_id')
