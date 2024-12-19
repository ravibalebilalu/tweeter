from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from tweetapp.models import Tweet
from tweetapp.serializers import TweetSerializer

@csrf_exempt
def tweet_list(request):
    if request.method == "GET":
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = TweetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return  JsonResponse(serializer.errors,status=400)
    

def tweet_detail(request,pk):
    try:
        tweet = Tweet.objects.get(pk=pk)
    except Tweet.DoesNotExist:
        return JsonResponse(status=404)
    
    if request.method == "GET":
        serializer = TweetSerializer(tweet)
        return JsonResponse(serializer.data)
    
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = TweetSerializer(tweet,tweet,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    elif request.method == "DELETE":
        tweet.delete()
        return HttpResponse(status=204)