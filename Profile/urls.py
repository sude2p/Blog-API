from django.urls import path
from .views import userRegister,userLogin, UserApi

urlpatterns = [
    path('register/', userRegister, name='register'),
    path('login/', userLogin, name='login'),
    # path('delete-user/<int:pk>', userDelete, name='delete_user'),
    path('userinfo/all/', UserApi.as_view(), name='userinfo'),
]