from django.urls import path
from .views import ActivityFeedApiView

urlpatterns = [
    path('activity/feed/', ActivityFeedApiView.as_view(), name='activity-feed'),
]