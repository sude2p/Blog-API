from django.db import models
from django.contrib.auth.models import User
from post.models import Post
from django.contrib.contenttypes.fields import GenericRelation  
from activity_feed.models import Activity  



# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    activity = GenericRelation(Activity)
   

