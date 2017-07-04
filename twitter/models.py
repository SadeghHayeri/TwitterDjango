from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    inherit = models.ForeignKey('self', related_name='children', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField('date published')
    body = models.CharField(max_length=140)

class Like(models.Model):
    post = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likedTime = models.DateTimeField('date liked')
