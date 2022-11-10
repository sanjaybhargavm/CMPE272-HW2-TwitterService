from django.urls import path

from . import views

## Author: Sanjay Bhargav Madamanchi and Abdul vahed Shaik
urlpatterns = [
    path('create_tweet/', views.create_tweet),
    path('get_timeline_tweets/', views.get_timeline_tweets),
    path('delete_tweet/', views.delete_tweet)
]
