from django.urls import path
from .views import *

urlpatterns=[
    path('like/all/', LikeApiView.as_view(), name='like-all'),
    path('likeid/<int:pk>/',LikeIdApiView.as_view(), name='likeid'),
   
]