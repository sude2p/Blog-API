from django.urls import path
from .views import *

urlpatterns=[
    path('comment/all/', CommentApiView.as_view(), name='comment-all'),
    path('commentid/<int:pk>/', CommentIdApiView.as_view(), name='comment-id'),
]