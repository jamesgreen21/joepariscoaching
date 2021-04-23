from django.urls import path
from . import views

app_name = 'journal'
urlpatterns = [
    path('', views.journal, name='index'),
    # path('<int:pk>/', views.workout, name='detail'),
    # path('<int:pk>/routine/<int:routine_id>/approach/<int:approach_id>/', views.approach, name='approach')
]