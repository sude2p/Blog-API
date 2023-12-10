from django.urls import path
from .views import *

urlpatterns = [
    path('post/data/', UserPostApiView.as_view(), name='user-post-data'),
    path('comment/data/', UserCommentApiView.as_view(), name='user-comment-data'),
    path('like/data/', UserLikeApiView.as_view(), name='user-like-data'),


]