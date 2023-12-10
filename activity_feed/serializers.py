from rest_framework import serializers
from post.serializers import PostSerializer
from comment.serializers import CommentSerializer
from like.serializers import LikeSerializer
from .models import Activity
from post.models import Post
from comment.models import Comment
from like.models import Like
from friends.models import Friends
from django.db.models import Q


# class ActivitySerializer(serializers.ModelSerializer):
#     user = serializers.SerializerMethodField()
#     content_object = serializers.SerializerMethodField()

#     class Meta:
#         model = Activity
#         fields = ['user', 'content_object', 'created_at']

#     def get_user(self, obj):
#         content_object = obj.content_object

#         if isinstance(content_object, Post):
#             user_data = {
#                 'id': content_object.author.id,
#                 'username': content_object.author.username,
#                 # Add other user fields as needed
#             }
#         elif isinstance(content_object, Comment):
#             user_data = {
#                 'id': content_object.user.id,
#                 'username': content_object.user.username,
#                 # Add other user fields as needed
#             }
#         elif isinstance(content_object, Like):
#             user_data = {
#                 'id': content_object.user.id,
#                 'username': content_object.user.username,
#                 # Add other user fields as needed
#             }
#         else:
#             user_data = {}

#         return user_data

#     def get_content_object(self, obj):
        
#         content_object = obj.content_object
#         if isinstance(content_object, Post):
#             return PostSerializer(content_object).data
#         elif isinstance(content_object, Comment):
#             return CommentSerializer(content_object).data
#         elif isinstance(content_object, Like):
#             return LikeSerializer(content_object).data
#         else:
#             return None
        
#    #------------------------------------------------------# 
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         friends_data = self.get_friends_data(instance)
#         likes_data = self.get_likes_data(instance)

#         data['friends'] = friends_data
#         data['likes'] = likes_data

#         return data

#     def get_friends_data(self, instance):
#         content_object = instance.content_object

#         if isinstance(content_object, Post):
#             content_user = content_object.author
#         elif isinstance(content_object, Comment):
#             content_user = content_object.user
#         elif isinstance(content_object, Like):
#             content_user = content_object.user
#         else:
#             return []

#         #  get friends based on both user and friend fields
        
#         friends_data = Friends.objects.filter(Q(user=content_user) | Q(friend=content_user)).values('friend__id', 'friend__username')
#         return friends_data
    

#     def get_likes_data(self, instance):
#         content_object = instance.content_object

#         if isinstance(content_object, Post):
#             user = content_object.author
#         elif isinstance(content_object, Comment):
#             user = content_object.user
#         elif isinstance(content_object, Like):
#             user = content_object.user
#         else:
#             return []

#         likes_data = Like.objects.filter(user=user).values('id', 'user__id')
#         return likes_data

class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    content_object = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['user', 'content_object', 'created_at']

    def get_user(self, obj):
        content_object = obj.content_object

        if isinstance(content_object, Post):
            user_data = {
                'id': content_object.author.id,
                'username': content_object.author.username,
                # Add other user fields as needed
            }
        elif isinstance(content_object, Comment):
            user_data = {
                'id': content_object.user.id,
                'username': content_object.user.username,
                # Add other user fields as needed
            }
        elif isinstance(content_object, Like):
            user_data = {
                'id': content_object.user.id,
                'username': content_object.user.username,
                # Add other user fields as needed
            }
        else:
            user_data = {}

        return user_data

    def get_content_object(self, obj):
        content_object = obj.content_object
        if isinstance(content_object, Post):
            return PostSerializer(content_object).data
        elif isinstance(content_object, Comment):
            return CommentSerializer(content_object).data
        elif isinstance(content_object, Like):
            return LikeSerializer(content_object).data
        else:
            return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        likes_data = self.get_likes_data(instance)

        data['likes'] = likes_data

        return data

    def get_likes_data(self, instance):
        content_object = instance.content_object

        if isinstance(content_object, Post):
            user = content_object.author
        elif isinstance(content_object, Comment):
            user = content_object.user
        elif isinstance(content_object, Like):
            user = content_object.user
        else:
            return []

        # Fetch likes for the authenticated user
        likes_data = Like.objects.filter(user=user).values('id', 'user__id')
        return likes_data