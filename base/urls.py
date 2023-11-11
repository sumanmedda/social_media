from django.urls import path
from . import views
# pk = primary key
urlpatterns = [
    # auth page
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerPage,name='register'),
    # home page
    path('', views.homePage, name="home"),
    # cruds of room
    path('room/<str:pk>', views.roomPage,name='room'),
    path('create-room/', views.createRoom,name='create-room'),
    path('update-room/<str:pk>', views.updateRoom,name='update-room'),
    path('delete-room/<str:pk>', views.deleteRoom,name='delete-room'),
    # delete message
    path('delete-message/<str:pk>', views.deleteMessage,name='delete-message'),
    # profile oage
    path('profile/<str:pk>', views.userProfile,name='user-profile'),
    path('update-user/', views.updateUser,name='update-user'),
    
]
