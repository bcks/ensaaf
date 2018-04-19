from django.contrib import admin
from django.urls import path, include
from data.views import *

urlpatterns = [
    path('profile/<int:id>/', profile, name="profile"),
    path('village/<slug:slug>/', village, name="village"),
    path('tehsil/<slug:slug>/', tehsil, name="tehsil"),
    path('district/<slug:slug>/', district, name="district"),
    path('search/', include('haystack.urls')),
    path('admin/', admin.site.urls),
    path('overview/', overview, name="overview"),
    path('<slug:directory>/<slug:slug>/', page),
    path('', home, name="home"),
    path('', home, name="home"),
]
