from django.db import models

# Create your models here.

class Like(models.Model):
    likeNum = models.IntegerField()
    isLikePushed = models.BooleanField(null=False)