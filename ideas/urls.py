from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('register/', views.register, name='register'),
    path('create/', views.create_idea, name='create_idea'),
    path('edit/<int:pk>/', views.edit_idea, name='edit_idea'),
    path('delete/<int:pk>/', views.delete_idea, name='delete_idea'),
    path('like/<int:pk>/', views.like_idea, name='like_idea'),
    path('comment/<int:pk>/', views.comment_idea, name='comment_idea'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]