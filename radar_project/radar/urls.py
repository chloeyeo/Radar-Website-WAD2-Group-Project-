from django.urls import path
from radar import views

app_name = 'radar'

urlpatterns = [
    path('', views.homepage1, name='homepage1'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('homepage/', views.homepage, name='homepage'),
    path('friendspage/', views.friendspage, name='friendspage'),
    path('account/', views.account, name='account'),

]
