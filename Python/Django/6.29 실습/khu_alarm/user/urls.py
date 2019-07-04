from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.sign_in, name ='sign_in'),
    path('sign_up/', views.sign_up, name ='sign_up'),
    path('user_list/', views.user_list, name = 'user_list')
]
