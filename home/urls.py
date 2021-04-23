from django.urls import path
from . import views as home
from marketing import views as marketing

app_name = 'home'
urlpatterns = [
    path('', home.index, name='index'),
    # path('subscribe/', marketing.email_list_subscription, name='subscribe'),
]