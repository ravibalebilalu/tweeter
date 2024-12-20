from django.urls import path,include
from tweetapp import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'tweets',views.TweetViewSet,basename="tweet")
router.register(r'users',views.UserViewSet,basename="user")

 
 
urlpatterns = [
    path("",include(router.urls))
]

 