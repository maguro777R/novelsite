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
    path('account/profile/', views.post_list, name='post_list'),
    path('signup/', views.signup_view, name='signup'),
    path('user/', views.user_view, name='user'),
    path('other/', views.other_view, name='other'),
    path('change_username/', views.UsernameChangeView.as_view(), name='change_username'),
    path('<str:username>/delete/', views.UserDeleteView.as_view(), name='delete'),
]