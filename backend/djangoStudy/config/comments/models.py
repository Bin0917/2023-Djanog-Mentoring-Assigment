from django.db import models
from users.models import User
from posts.models import Post
# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    reply = models.CharField(max_length=70)
    content = models.CharField(max_length=70)