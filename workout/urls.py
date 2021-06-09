from django.urls import path
from . import views

app_name = 'workout'
urlpatterns = [
    path('<int:pk>/', views.WorkoutView.as_view(), name='workout-view'), # pk=journal.id 
    path('<int:pk>/set/<int:approach_id>/progress/', views.progress_create, name='create-progress'), # pk=journal.id 
    path('<int:pk>/edit/', views.progress_edit, name='edit-progress'), # pk=progress.id
    # path('<int:pk>/skip/<int:approach_id>/', views.skip_set, name='skip_set'),
    # path('<int:pk>/update/<int:progress_id>/', views.workout_update, name='update-progress'),
    path('<int:pk>/complete/', views.complete_workout, name='complete') # pk=journal.id 
]