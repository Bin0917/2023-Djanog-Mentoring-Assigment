from django.db import models

# Create your models here.

# class Like(models.Model):
#     likeNum = models.IntegerField()
#     isLikePushed = models.BooleanField(null=False)
    
class Like(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)