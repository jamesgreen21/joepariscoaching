from django.contrib import admin
from .models import Routine, Workout, Exercise, Equipment, Approach, Perform, Instructions, WorkoutSet


# class ApproachAdminInline(admin.TabularInline):
#     model = Approach
#     fields = [
#         'set_number',
#         'reps_targetted',
#         'perform_id'
#     ]


# class RoutineInstanceInline(admin.TabularInline):
#     model = Routine


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass


# @admin.register(Approach)
# class ApproachAdmin(admin.ModelAdmin):
#     list_display = ('id', 'routine_id')


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_filter = ('bodypart', 'exercise_type')


@admin.register(Instructions)
class InstructionsAdmin(admin.ModelAdmin):
    pass


class WorkoutSetInstanceInline(admin.TabularInline):
    model = WorkoutSet


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    fields  = ['name', 'tag']
    list_display  = ('name', 'tag')
    inlines = [
        WorkoutSetInstanceInline
    ]


# @admin.register(Routine)
# class RoutineBuilderAdmin(admin.ModelAdmin):
#     fields = ['workout_id', 'exercise_id', 'order']
#     list_display  = ('workout_id', 'exercise_id')
#     inlines = [
#         ApproachAdminInline
#     ]