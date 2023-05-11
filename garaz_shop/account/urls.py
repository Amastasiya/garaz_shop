from django.urls import path
from django.urls import re_path as url
from django.urls import include
from . import views

urlpatterns = [
    # post views
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('', views.garaz, name='garaz'),
    path('login/', include("django.contrib.auth.urls"), name='login'),
    path('logout/', include("django.contrib.auth.urls"), name='logout'),
    path('logout-then-login/', include("django.contrib.auth.urls"), name='logout_then_login'),

]