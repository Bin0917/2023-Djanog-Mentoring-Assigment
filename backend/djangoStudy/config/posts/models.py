from django.db import models
from users.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    content = models.CharField(max_length=1000)
    title = models.CharField(max_length=100)
    