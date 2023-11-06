from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=50)
#     nickname = models.CharField(max_length=50)
#     #settings.py 에 이미지 저장 경로 추가
#     profileImage = models.ImageField(upload_to='community', null=True)   
    
    
class User(AbstractUser):
    #settings.py 에 이미지 저장 경로 추가
    profileImage = models.ImageField(upload_to='pictures', null=True)   
    