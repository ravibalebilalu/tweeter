from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tweetapp.models import Tweet
from tweetapp.serializers import TweetSerializer


@api_view(["GET","POST"])
def tweet_list(request,format=None):
    if request.method == "GET":
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(["GET","PUT","DELETE"])
def tweet_detail(request,pk,format=None):

    try:
        tweet = Tweet.objects.get(pk=pk)
    except Tweet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = TweetSerializer(tweet)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TweetSerializer(tweet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        tweet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
