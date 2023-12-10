from rest_framework import serializers
from .models import Friends

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ['user', 'friend']