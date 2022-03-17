from django.urls import path
from radar import views

app_name = 'radar'

urlpatterns = [
    path('', views.homepage1, name='homepage1'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('homepage1/', views.homepage1, name='homepage1'),
    path('account/', views.account, name='account'),
    path('logout/', views.user_logout, name='logout'),
]
