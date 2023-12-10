from django.urls import path
from .views import *

urlpatterns=[
    path('friends/', FriendsApiView.as_view(), name='friend-list-create'),
     path('friends/<int:pk>/', FriendsApiView.as_view(), name='friend-del-view')
]