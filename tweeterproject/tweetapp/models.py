from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    tweet_text = models.TextField(max_length=200)
    creater = models.ForeignKey('auth.user',related_name="tweets",on_delete=models.CASCADE)

