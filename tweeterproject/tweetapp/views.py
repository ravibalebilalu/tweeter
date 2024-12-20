from tweetapp.models import Tweet
from tweetapp.serializers import TweetSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from tweetapp.serializers import UserSerializer
from rest_framework import permissions
from tweetapp.permisions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

class TweetList(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(creater=self.request.user)

class TweetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view (["GET"])
def api_root(request,format=None):
    return Response({
        "users":reverse("user-list",request=request,format=format),
        "tweets":reverse("tweet-list",request=request,format=format)
    })

    

