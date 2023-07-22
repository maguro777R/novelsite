from django.conf.urls import include
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('signup/', views.signup_view, name='signup'),
    path('user/', views.user_view, name='user'),
    path('other/', views.other_view, name='other'),
    path('change_username/', views.UsernameChangeView.as_view(), name='change_username'),
    path('<str:username>/delete/', views.UserDeleteView.as_view(), name='delete'),
    path('user_post_list/', views.user_post_list, name='user_post_list'),
    path('post/<int:pk>/delete_post/', views.delete_post, name='delete_post'),
    path('search/', views.PostListView.as_view(), name='search'),
    path('notice/', views.NoticeListView.as_view(), name='notice'),
    path('terms/', views.terms, name='terms'),
    path('category/<str:category>/', views.category, name='category'),
    path('tag/<str:tag>/', views.tag, name='tag'),
]