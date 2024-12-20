from rest_framework import serializers
from tweetapp.models import Tweet
from django.contrib.auth.models import User

class TweetSerializer(serializers.ModelSerializer):
    creater = serializers.ReadOnlyField(source="creater.username")
    class Meta:
        model = Tweet
        fields = ["id","tweet_text","created_at","creater"]
        


class UserSerializer(serializers.ModelSerializer):
    tweets = serializers.PrimaryKeyRelatedField(many=True,queryset=Tweet.objects.all())

    class Meta:
        model = User
        fields = ["id","username","tweets"]
    