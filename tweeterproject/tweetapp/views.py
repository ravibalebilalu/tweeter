from tweetapp.models import Tweet
from tweetapp.serializers import TweetSerializer
from django.contrib.auth.models import User
from tweetapp.serializers import UserSerializer
from rest_framework import permissions
from tweetapp.permisions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
 


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
         


 

@api_view (["GET"])
def api_root(request):
    return Response({
        "users":reverse("user-list",request=request,format=format),
        "tweets":reverse("tweet-list",request=request,format=format)
    })

    

