
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('tweetapi/', include('tweetapi.urls')),
]


