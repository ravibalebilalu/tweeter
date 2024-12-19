from rest_framework import serializers
from tweetapp.models import Tweet

class TweetSerializer(serializers.Mod):
    class Meta:
        model = Tweet
        fields = ["id","tweet_text"]
    