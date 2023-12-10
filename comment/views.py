from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCommentOwner
from .serializers import CommentSerializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import GenericAPIView
from .models import Comment

# Create your views here.

class CommentApiView(GenericAPIView):
    queryset = Comment.objects.select_related('post','user')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsCommentOwner]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # search_fields =[]
    filterset_fields =['post','user']
#------------------------function to view all the comment of all the users------------------#
    def get(self, request):
        queryset = self.get_queryset()
        filter_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filter_queryset, many=True)
        return Response(serializer.data)

#-----------------------------------------------------------------------------------------#

#------------------------function to post comment for the authenticated user-----------#   
    def post(self, request):

        # Assign the user ID to the 'user' key in the request data
        request.data['user'] = request.user.id

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
        
         serializer.save()
         return Response({'post':'comment posted successfully!'})
        else:
         return Response(serializer.errors)

#-----------------------------------------------------------------------------------------#   

class CommentIdApiView(GenericAPIView):
   queryset = Comment.objects.select_related('post','user')
   serializer_class = CommentSerializer
   permission_classes = [IsAuthenticated, IsCommentOwner]

#------------------------function to view comment for the authenticated user as per passing id-----------#

   def get(self, request, pk):
      try:
         queryset = Comment.objects.get(id=pk)
      except:
         return Response({'error':'data does not exist!!'})

      serializer = self.serializer_class(queryset)
      return Response(serializer.data)
#-----------------------------------------------------------------------------------------#    

#------------------------function update  comment for the authenticated user as per passing id-----------# 

   def put(self, request, pk):
      queryset = Comment.objects.get(id=pk)
      self.check_object_permissions(request, queryset)
      serializer = self.serializer_class(queryset, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response({'message':'Data updataed!'})
      else:
         return Response(serializer.errors)
#-----------------------------------------------------------------------------------------# 

#------------------------function delete blogpost  for the authenticated user as per passing id-----------#
   def delete(self, request, pk):
      queryset = Comment.objects.get(id=pk)
      self.check_object_permissions(request, queryset)
      queryset.delete()
      return Response({'message':'Data deleted!'})
#-----------------------------------------------------------------------------------------#     