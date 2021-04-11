from django.contrib import admin
from .models import Routine, Workout, Exercise, Equipment, Approach, Perform


class ApproachAdminInline(admin.TabularInline):
    model = Approach
    fields = [
        'set_number',
        'reps_targetted',
        'weight_targetted',
        'perform_id'
    ]


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_filter = ('bodypart', 'exercise_type')


@admin.register(Perform)
class PerformAdmin(admin.ModelAdmin):
    pass


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    fields  = ['name', 'tag']
    list_display  = ('name', 'tag')


@admin.register(Routine)
class RoutineBuilderAdmin(admin.ModelAdmin):
    fields = ['workout_id', 'exercise_id', 'order']
    list_display  = ('workout_id', 'exercise_id')
    inlines = [
        ApproachAdminInline
    ]