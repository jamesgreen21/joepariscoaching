from django.contrib import admin
from .models import Journal, Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_filter = ('subject', 'journal_id')


@admin.register(Journal)
class JournalBuilderAdmin(admin.ModelAdmin):
    fields = ['entry_date', 'user_id', 'workout_id']
    list_display  = ('entry_date', 'user_id', 'workout_id')
