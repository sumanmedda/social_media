from django.urls import path
from . import views
# pk = primary key
urlpatterns = [
    path('', views.homePage, name="home"),
    path('room/<str:pk>', views.roomPage,name='room'),
    path('profile/<str:pk>', views.profilePage,name='profile'),
    path('create-room/', views.createRoom,name='create-room'),
    path('update-room/<str:pk>', views.updateRoom,name='update-room'),
    path('delete-room/<str:pk>', views.deleteRoom,name='delete-room'),
]
