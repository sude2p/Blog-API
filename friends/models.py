from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation 
from activity_feed.models import Activity  

# Create your models here.

class Friends(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_friends')
    activity = GenericRelation(Activity)