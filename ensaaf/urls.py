from django.contrib import admin
from django.urls import path, include
from data.views import *

urlpatterns = [
    path('profile/<int:id>/', profile, name="profile"),
    path('village/<int:id>/', village, name="village"),
    path('search/', include('haystack.urls')),
    path('admin/', admin.site.urls),
    path('', home, name="home"),
]
