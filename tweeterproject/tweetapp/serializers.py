from rest_framework import serializers
from tweetapp.models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ["id","tweet_text","created_at"]
    