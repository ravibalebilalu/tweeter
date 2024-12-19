from django.urls import path
from tweetapp.models import Tweet
from tweetapp import views

urlpatterns = [
    path("tweets/",views.tweet_list),
    path("tweets/<int:pk>/",views.tweet_detail),
]
