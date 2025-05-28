# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_list, name='users-list'),
    path('<int:id>/', views.user_detail, name='user-detail'),
]
