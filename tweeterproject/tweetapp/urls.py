from django.urls import path
from tweetapp.models import Tweet
from tweetapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("tweets/",views.TweetList.as_view()),
    path("tweets/<int:pk>/",views.TweetDetail.as_view()),
]

urlpatterns  = format_suffix_patterns(urlpatterns)