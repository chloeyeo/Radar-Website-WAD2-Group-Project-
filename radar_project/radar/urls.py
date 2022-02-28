from django.urls import path
from radar import views

app_name = 'radar'

urlpatterns = [
    path('', views.index, name='index'),
]
