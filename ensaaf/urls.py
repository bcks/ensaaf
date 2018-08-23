from django.contrib import admin
from django.urls import path, include
from data.views import *

from django.conf import settings
from django.conf.urls import include, url
from graphene_django.views import GraphQLView

urlpatterns = [
    path('profile/<int:id>/', profile, name="profile"),
    path('village/<slug:slug>/', village, name="village"),
    path('tehsil/<slug:slug>/', tehsil, name="tehsil"),
    path('district/<slug:slug>/', district, name="district"),
    path('year/<year>/', year, name="year"),
    path('locality/<int:id>/', locality, name="locality"),
    path('securityforce/<slug:slug>/', securityforce, name="securityforce"),
    url(r'^detention/(?P<type>[0-9]+)/(?P<name>[A-Za-z0-9 \/+_\-]+)/$', detention, name="detention"),
    path('official/<slug:slug>/', official, name="official"),
    path('search/', include('haystack.urls')),
    path('admin/', admin.site.urls),
    path('overview/', overview, name="overview"),
    path('map_ajax/', map_ajax, name="map_ajax"),
    path('change/', change, name="change"),
    path('profiles/', profiles, name="profiles"),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
    path('<slug:slug>/', page),
    path('', map, name="map"),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

