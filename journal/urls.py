from django.urls import path
from . import views

app_name = 'journal'
urlpatterns = [
    path('checkin/', views.checkin, name='checkin'),
    path('', views.JournalListView.as_view(), name='index'),
    path('<int:pk>/', views.JournalDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.JournalUpdateView.as_view(), name='edit'),
    path('<int:pk>/workout/<int:workout_id>/complete/', views.WorkoutCompleteView.as_view(), name='workout-complete'),
    path('<int:journal_id>/workout/<int:pk>/', views.WorkoutDetailView.as_view(), name='workout-view'),
    path('<int:journal_id>/workout/<int:workout_id>/set/<int:workoutset>/<int:pk>/', views.ProgressUpdateView.as_view(), name='workout-edit'),
    path('<int:journal_id>/workout/<int:workout_id>/set/<int:workoutset>', views.ProgressCreateView.as_view(), name='workout-new'),
]