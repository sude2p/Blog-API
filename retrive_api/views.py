from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password

from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from post.serializers import PostSerializer
from comment.serializers import CommentSerializer
from like.serializers import LikeSerializer
from post.models import Post
from comment.models import Comment
from like.models import Like

from rest_framework.generics import ListAPIView

#Create your views here.

class UserPostApiView(GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    def get(self,request):
    
      request.data['author'] = request.user.id
      queryset = self.queryset.filter(author=request.user)
      
      serializer = self.serializer_class(queryset, many=True)
      return Response(serializer.data)

# class UserPostApiView(ListAPIView):
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         # Retrieve posts for the authenticated user
#         return Post.objects.filter(author=self.request.user)

class UserCommentApiView(GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    def get(self,request):
    
      request.data['user'] = request.user.id
      queryset = self.queryset.filter(user=request.user)
      
      serializer = self.serializer_class(queryset, many=True)
      return Response(serializer.data)
    

class UserLikeApiView(GenericAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
      
      request.data['user'] = request.user.id
      queryset = self.queryset.filter(user=request.user)
      print(f"Like queryset: {queryset}")
      serializer = self.serializer_class(queryset, many=True)
      return Response(serializer.data)
