from django.urls import path
from . import views

urlpatterns = [
  path('theme/<slug>', views.theme, name='theme'),
  path('themes', views.themes, name='themes'),
  path('clip/<slug>', views.clip, name='clip'),
  path('video/<slug>', views.video, name='video'),
  path('search', views.search, name='search'),
  path('interviews', views.interviews, name='interviews'),
  path('about', views.about, name='about'),
  path('', views.interviews_home, name='interviews_home'),
]
