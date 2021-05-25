from django.urls import path
from . import views

app_name = 'journal'
urlpatterns = [
    path('', views.journal, name='index'),
    path('checkin/', views.checkin, name='checkin'),
    # path('<int:pk>/routine/<int:routine_id>/approach/<int:approach_id>/', views.approach, name='approach')
]