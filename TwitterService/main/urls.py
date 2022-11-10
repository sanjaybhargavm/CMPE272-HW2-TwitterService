from django.urls import path

from . import views

## Author: Sanjay Bhargav Madamanchi

urlpatterns = [
    path('home/',views.load_home_page, name='home'),
]
