from django.urls import path
from radar import views

app_name = 'radar'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('homepage1/', views.homepage1, name='homepage1'),
    path('homepage2/', views.homepage2, name='homepage2'),
    path('friendspage/', views.friendspage, name='friendspage'),
    path('account/', views.account, name='account'),

]
