from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('room/', views.roomPage,name='room'),
    path('profile/', views.profilePage,name='profile'),
]
