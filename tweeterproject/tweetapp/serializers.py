from rest_framework import serializers
from tweetapp.models import Tweet
from django.contrib.auth.models import User

class TweetSerializer(serializers.HyperlinkedModelSerializer):
    creater = serializers.ReadOnlyField(source="creater.username")
     
    class Meta:
        model = Tweet
        fields = ["url", "id","tweet_text","created_at","creater"]
        


class UserSerializer(serializers.HyperlinkedModelSerializer):
    tweets = serializers.HyperlinkedRelatedField(many=True,view_name="tweet-detail",read_only=True)

    class Meta:
        model = User
        fields = ["url", "id","username","tweets"]
    