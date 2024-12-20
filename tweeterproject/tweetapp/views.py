from tweetapp.models import Tweet
from tweetapp.serializers import TweetSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from tweetapp.serializers import UserSerializer
from rest_framework import permissions
from tweetapp.permisions import IsOwnerOrReadOnly

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

    

