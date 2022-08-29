from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('room/', views.Room, name='room'),
    path('new/', views.Create, name='new'),
    path('join/', views.Join, name='join'),
    path('get_token/', views.getToken, name='getToken'),
    path('create-member/', views.newMeeting, name='createMember'),
    path('join-member/', views.joinMeeting, name='joinMeeting'),
    path('get-member/', views.getMember, name='getMember'),
    path('delete-member/', views.deleteMember, name='deleteMember'),
    path('agenda/', views.Agenda, name='Agenda'),

]