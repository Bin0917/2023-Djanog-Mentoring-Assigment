from django.db import models
from users.models import User
from likes.models import Like
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    title = models.CharField(max_length=100)
    views = models.IntegerField()
    likeNum = models.ForeignKey(Like, on_delete=models.CASCADE)
    writtenDate = models.DateField(auto_now=False, auto_created=True)
    
    
    