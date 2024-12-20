from django.urls import path
from tweetapp.models import Tweet
from tweetapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("",views.api_root,name="tweets"),
    path("tweets/",views.TweetList.as_view(),name="tweet-list"),
    path("tweets/<int:pk>/",views.TweetDetail.as_view(),name="tweet-detail"),
    path("users/",views.UserList.as_view(),name="user-list"),
    path("users/<int:pk>/",views.UserDetail.as_view(),name="user-detail"),
]

urlpatterns  = format_suffix_patterns(urlpatterns)