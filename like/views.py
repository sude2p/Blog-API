from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsLikeOwner
from .serializers import LikeSerializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import GenericAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Like



# Create your views here.

class LikeApiView(GenericAPIView):
    queryset = Like.objects.select_related('user','content_type')
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated, IsLikeOwner]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # search_fields =[]
    filterset_fields =['content_type','user']
#------------------------function to view all the like of all the users------------------#
    def get(self, request):
        queryset = self.get_queryset()
        filter_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filter_queryset, many=True)
        return Response(serializer.data)

# -----------------------------------------------------------------------------------------#

#------------------------function to post like for the authenticated user-----------#   
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

class LikeIdApiView(GenericAPIView):
   queryset = Like.objects.select_related('user','content_type')
   serializer_class = LikeSerializer
   permission_classes = [IsAuthenticated, IsLikeOwner]

#------------------------function to view like for the authenticated user as per passing id-----------#

   def get(self, request, pk):
      try:
         queryset = Like.objects.get(id=pk)
      except:
         return Response({'error':'data does not exist!!'})

      serializer = self.serializer_class(queryset)
      return Response(serializer.data)
#-----------------------------------------------------------------------------------------#    
 #------------------------function update  like for the authenticated user as per passing id-----------# 

   def put(self, request, pk):
      queryset = Like.objects.get(id=pk)
      self.check_object_permissions(request, queryset)
      serializer = self.serializer_class(queryset, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response({'message':'Data updataed!'})
      else:
         return Response(serializer.errors)
#-----------------------------------------------------------------------------------------# 

#------------------------function delete like for the authenticated user as per passing id-----------#
   def delete(self, request, pk):
      queryset = Like.objects.get(id=pk)
      self.check_object_permissions(request, queryset)
      queryset.delete()
      return Response({'message':'Data deleted!'})
#-----------------------------------------------------------------------------------------#     
