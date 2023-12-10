from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from activity_feed.models import Activity

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200,null=False, blank=False,default='My Blog')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # the Post model allows instances of Post to have a generic relationship with instances of the Activity model#
    activity = GenericRelation(Activity)

    # def __str__(self):
    #     return self.title
    
 