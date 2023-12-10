from rest_framework import serializers
from .models import Comment
from django.contrib.auth.models import User
from post.models import Post

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id','username']

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['id','author','title','content','created']

# class CommentSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     post = PostSerializer()

#     class Meta:
#         model = Comment
#         fields = ['id', 'post', 'content_comment', 'user','created']

#     def create(self, validated_data):
#         user_data = validated_data.pop('user')
#         post_data = validated_data.pop('post')

#         user_instance = User.objects.create(**user_data)
#         post_instance = Post.objects.create(**post_data)

#         comment_instance = Comment.objects.create(user=user_instance, post=post_instance, **validated_data)
#         return comment_instance


class CommentSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Comment
        fields = ['id','post','user','content_comment','created_at']