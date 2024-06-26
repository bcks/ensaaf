from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('interviews_map_xhr/', views.interviews_map_xhr, name="interviews_map_xhr"),
    path('interviews_gallery_xhr/', views.interviews_gallery_xhr, name="interviews_gallery_xhr"),
    path("theme/<slug>", views.theme, name="theme"),
    path("themes", views.themes, name="themes"),
    path("clip/<id>", views.clip, name="clip"),
    path("transcript/<id>/<starttime>/<endtime>/<currenttime>/", views.transcript, name="transcript"),
    path("video/<id>", views.video, name="video"),
    path("search", views.search, name="search"),
    path("interviews", views.interviews, name="interviews"),
    path("gallery", views.gallery, name="gallery"),
    path("about", views.about, name="about"),
    path("", views.interviews_home, name="interviews_home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


