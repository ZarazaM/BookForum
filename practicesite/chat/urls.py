from django.urls import path

from . import views

# app_name = 'chat'
urlpatterns = [
    path('', views.allChats, name='indexchats'),
    path('<int:chat_id>/', views.specificChat, name='specific'),
    path('send', views.send, name='sendtochat'),
    path('getmessages/<int:chat_id>', views.getMessages, name='getMessages'),
    path('createchat', views.createChat, name='createChat')
]