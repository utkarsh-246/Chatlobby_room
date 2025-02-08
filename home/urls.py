from home import views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  
    path(' ', views.chatlobby, name='chatlobby'),
    path('lobby/create_lobby/', views.create_lobby, name='create_lobby'),
    path('lobby/', views.lobby, name='lobby')
]
