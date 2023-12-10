from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class PostApiView(GenericAPIView):
   queryset = Post.objects.select_related('author')
   serializer_class = PostSerializer
   permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
   filter_backends = [DjangoFilterBackend, filters.SearchFilter]
   filterset_fields = ['author']
   search_fields = ['title','created']
#------------------------function to view all the post of all the users------------------#
   def get(self,request):
      queryset = self.get_queryset()
      filter_queryset = self.filter_queryset(queryset)
      serializer = self.serializer_class(filter_queryset, many=True)
      return Response(serializer.data)
#-----------------------------------------------------------------------------------------#

#------------------------function to post in the blog for the authenticated user-----------#   
   def post(self, request):
      # Explicitly set the author from the request user
      request.data['author'] = request.user.id
      serializer = self.serializer_class(data=request.data)
      if serializer.is_valid():
        
         serializer.save()
         return Response({'post':'blog posted successfully!'})
      else:
         return Response(serializer.errors)

#-----------------------------------------------------------------------------------------#   

 

class PostIdApiVIew(GenericAPIView):
   queryset = Post.objects.select_related('author')
   serializer_class = PostSerializer    
   permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

#------------------------function to view blogpost for the authenticated user as per passing id-----------# 
   
   def get(self, request, pk):
      try:
         queryset = Post.objects.get(id=pk)
      except:
         return Response({'error':'data not found'})   
      
      serializer = self.serializer_class(queryset)
      return Response(serializer.data)
#-----------------------------------------------------------------------------------------#  

#------------------------function update  blogpost for the authenticated user as per passing id-----------# 
   def put(self, request, pk):
      queryset = Post.objects.get(id=pk)
      self.check_object_permissions(request, queryset)
      serializer = self.serializer_class(queryset, data=request.data, partial=True)
      # serializer.fields['author'].read_only = True                                  
      if serializer.is_valid():
         serializer.save()
         return Response({'message':'Data updataed!'})
      else:
         return Response(serializer.errors)
#-----------------------------------------------------------------------------------------#  

#------------------------function delete blogpost  for the authenticated user as per passing id-----------#
   def delete(self, request, pk):
      queryset = Post.objects.get(id=pk)
      self.check_object_permissions(request, queryset)
      queryset.delete()
      return Response({'message':'Data deleted!'})
#-----------------------------------------------------------------------------------------#  


