from django.urls import path
from radar import views

app_name = 'radar'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('account/<slug:current_user_slug>/', views.account, name='account'),
    path('logout/', views.user_logout, name='logout'),
    path('search_results/', views.search_results, name='search_results'),
    path('category/<slug:category_name_slug>/',
         views.show_category, name='show_category'),
    path('addPost/', views.add_post, name='addPost'),
    path('like_post/', views.LikePostView.as_view(), name='like_post'),
    path('post/<slug:post_title_slug>/', views.show_post, name='post'),

]
