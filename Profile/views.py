from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from .serializers import ProfileSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import *

# Create your views here.

#---------------------User Registration--------------------------------------------------#
@api_view(['POST'])
@permission_classes([AllowAny])
def userRegister(request):
    password = request.data.get('password')
    request.data['password'] = make_password(password) # make password function changes user password to encrypted
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
       
        return Response('User Successfully Created!')
    else:
        return Response(serializer.errors)
    
#-------------------------------------------------------------------------------------------#

#----------------------------------User Login------------------------------------------------#  
@api_view(['POST'])
@permission_classes([AllowAny])
def userLogin(request):
    
    username = request.data.get('username')
    password = request.data.get('password')

    # try:
    #     username = User.objects.get(username=username)
    # except:
    #     return Response('Username doesnot exist')
    if not User.objects.filter(username=username).exists():
        return Response({'error':'Username doesnot exists!'})   

    user = authenticate(username=username, password=password)
    if user is not None:
        token,_ = Token.objects.get_or_create(user=user)
        return Response({'token':token.key})
    else:
        return Response({'error':'Invalid username or password!!'})



#-------------------------------------------------------------------------------------------# 
# 
# ----------------------------------Delete User------------------------------------------------# 
# @api_view(['POST'])
# def userDelete(request, pk):
#     profile = User.objects.get(id=pk)
#     profile.delete()
#     return Response({'message':'user successfully deleted!'})

#----------------------------------users API view------------------------------------------------# 
class UserApi(GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes =[IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['user__first_name','user__last_name']
    filterset_fields =['user__username']

    def get(self, request):
        queryset = self.get_queryset()
        filter_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filter_queryset, many=True)
        return Response(serializer.data)



#-------------------------------------------------------------------------------------------#

