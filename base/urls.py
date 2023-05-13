from django.contrib import admin
from django.urls import path , include
from base import views

urlpatterns = [
    path('' , views.register , name='register'),
    path('login' , views.login_view , name='login'),
    path('home' , views.home , name='home'),
    path('meeting' , views.videocall , name='meeting'),
    path('join/',views.join_room, name='join_room'),
    path('logout/',views.logout_view, name='logout'),

]
