from django.db import models
from users.models import User
from likes.models import Like
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    content = models.CharField(max_length=1000)
    title = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    writtenDate = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='pictures', null=True)
    likes = models.ManyToManyField(
        User, # User 모델과 Blog 모델을 M:N 관계로 두겠다.
        related_name = 'likes'
    )
    def __str__(self):
        return self.title
