from django.urls import path
from .views import *

urlpatterns =[
    path('postinfo/all/', PostApiView.as_view(), name='postinfo'),
    path('postidinfo/<int:pk>/', PostIdApiVIew.as_view(), name='postid'),
   
]