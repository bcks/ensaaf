from django.contrib import admin
from django.urls import path, include
from data.views import *

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from graphene_django.views import GraphQLView


urlpatterns = i18n_patterns(
    path('', map, name='map'),
    path('all_profiles/<slug:slug>/', all_profiles, name="all_profiles"),
    path('map_ajax/', map_ajax, name="map_ajax"),
    path('email/', emailView, name='email'),
    path('profiles/', profiles, name="profiles"),
    path('perpetrators/', perpetrators, name="perpetrators"),
    path('villages/', villages, name="villages"),
    path('overview/', overview, name="overview"),
    path('change/', change, name="change"),
    path('detail/', detail, name="detail"),
    path('profile/<slug:record_id>/', profile, name="profile"),
    path('village/<slug:slug>/', village, name="village"),
    path('tehsil/<slug:slug>/', tehsil, name="tehsil"),
    path('district/<slug:slug>/', district, name="district"),
    path('year/<year>/', year, name="year"),
    path('locality/<slug:slug>/', locality, name="locality"),
    path('official/S0001/detail', official_detail, name="official_detail"),
    path('official/S0001/detail/', official_detail, name="official_detail"),
    path('official/<slug:slug>/', official, name="official"),
    url(r'^search/', include('haystack.urls')),
    path('cremation/<slug:slug>/', cremation, name="cremation"),
    path('securityforce/<slug:slug>/', securityforce, name="securityforce"),
    url(r'^detention/(?P<type>[0-9]+)/(?P<name>[A-Za-z0-9 \/+_\-]+)/$', detention, name="detention"),
    path('success/', successView, name='success'),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secret-admin-login/', admin.site.urls),
    path('search/spelling/', spelling, name='spelling'),
    path('search/autocomplete/', autocomplete, name='autocomplete'),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
    path('vikus/data/', vikusdata, name="vikusdata"),
#    path('tinymce/', include('tinymce.urls')),
    path('<slug:slug>/', page),
    prefix_default_language=False 
) 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

