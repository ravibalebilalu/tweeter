from django.db import models

class Tweet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    tweet_text = models.TextField(max_length=200)

