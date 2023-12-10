from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Friends
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import FriendSerializer
from rest_framework.generics import GenericAPIView

# Create your views here.
class FriendsApiView(ListCreateAPIView, DestroyAPIView):
    queryset = Friends.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# class FriendsApiView(GenericAPIView):
#     queryset = Friends.objects.select_related('user1','user2')
#     serializer_class = FriendSerializer
#     permission_classes = [IsAuthenticated]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['user1','user2']

#     def get(self, request):
#         queryset = self.get_queryset()
#         filter_queryset = self.filter_queryset(queryset)
#         serializer = self.serializer_class(filter_queryset, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         # Assign the user ID to the 'user1' key in the request data
#         request.data['user1'] = request.user.id
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'post':'friend added successfully!'})
#         else:
#             return Response(serializer.errors)

#     def delete(self, request, pk):
#         # Delete a friend by ID
#         friend = self.get_object(pk)
#         friend.delete()
#         return Response({'post':'friend removed successfully!'})