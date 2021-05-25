from django.urls import path
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views


app_name = 'accounts'
urlpatterns = [
    path('', accounts_views.profile, name='profile'),
]
