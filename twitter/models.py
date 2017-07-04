from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    replyTo = models.ForeignKey('self', on_delete=models.CASCADE, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateTimeField('date published')
    body = models.CharField(max_length=140)

class Like(models.Model):
    post = models.OneToOneField(Tweet, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    likedTime = models.DateTimeField('date liked')
