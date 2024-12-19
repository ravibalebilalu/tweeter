from django.urls import path
from tweetapp.models import Tweet
from tweetapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("tweets/",views.tweet_list),
    path("tweets/<int:pk>/",views.tweet_detail),
]

urlpatterns  = format_suffix_patterns(urlpatterns)