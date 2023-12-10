from django.db.models import Q 
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from friends.models import Friends
from .models import Activity
from post.models import Post
from comment.models import Comment
from like.models import Like
from .serializers import ActivitySerializer
from itertools import chain

class ActivityFeedApiView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Fetch friends of the authenticated user
        # friends = Friends.objects.filter(user=request.user).values_list('friend', flat=True)

        # Fetch activities related to the authenticated user
        post_activities = Post.objects.filter(author=request.user).select_related('author')[:10]
        comment_activities = Comment.objects.filter(user=request.user).select_related('user')[:10]
        like_activities = Like.objects.filter(user=request.user).select_related('user')[:10]

        # Combine all activities
        activities_queryset = list(chain(post_activities, comment_activities, like_activities))

        # Update the activities to have a 'content_object' attribute
        for activity in activities_queryset:
            # Explicitly check the type of activity and set content_object accordingly
            if isinstance(activity, Post):
                setattr(activity, 'content_object', activity)
            elif isinstance(activity, Comment):
                setattr(activity, 'content_object', activity)
            elif isinstance(activity, Like):
                setattr(activity, 'content_object', activity)

        serializer = ActivitySerializer(activities_queryset, many=True)
        return Response(serializer.data)
    


# class ActivityFeedApiView(GenericAPIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         friends = Friends.objects.filter(user=request.user).values_list('friend', flat=True)
#         # user_friends = Friends.objects.filter(Q(user=request.user) | Q(friend=request.user)).values_list('friend', flat=True)
#         # Ensure you are selecting related objects when querying activities
#         post_activities = Post.objects.filter(author__in=friends).select_related('author')[:10]
#         comment_activities = Comment.objects.filter(user__in=friends).select_related('user')[:10]
#         like_activities = Like.objects.filter(user__in=friends).select_related('user')[:10]

#         activities_queryset = list(chain(post_activities, comment_activities, like_activities))

#         # Update the activities to have a 'content_object' attribute
#         for activity in activities_queryset:
#             # Explicitly check the type of activity and set content_object accordingly
#             if isinstance(activity, Post):
#                 setattr(activity, 'content_object', activity)
#             elif isinstance(activity, Comment):
#                 setattr(activity, 'content_object', activity)
#             elif isinstance(activity, Like):
#                 setattr(activity, 'content_object', activity)

#         serializer = ActivitySerializer(activities_queryset, many=True)
#         return Response(serializer.data)
       
        


