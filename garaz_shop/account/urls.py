from django.urls import path
from . import views

urlpatterns = [
    # post views
    # path('', views.index, name='vhod'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
]