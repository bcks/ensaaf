from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache import cache
from django.contrib import messages
from django.db.models import OuterRef, Subquery, Count, Sum
from django.template.defaulttags import register

from .models import *
from django.shortcuts import render
from .utils import calculate_stats




def home(request):    
    all = Data.objects.all();
    victims = all.order_by('?')[:20]    
    stats = calculate_stats(all)    
    return render(request, "home.html", { 
      "victims": victims,
      "stats": stats
      })


def profile(request, id=None):
    queryset = Data.objects.filter(record_id=id)
    victim = queryset[:1].get()
    if victim.village_id:
      try:
        village = Villages.objects.filter(id=victim.village_id)[:1].get()
      except Villages.DoesNotExist:
          village = None
    else:
      village = None
    if id is not None and victim is None:
        return messages.warning(request,"Profile %s was not found"%id)
    return render(request, "profile.html", { "victim": victim, "village":village } )


def village(request, slug=None):
    victims = Data.objects.filter(village_id=slug).order_by('victim_name')
    village = Villages.objects.filter(id=slug)[:1].get()
    if id is not None and id is None:
        return messages.warning(request,"Village %s was not found"%id)
    return render(request, "village.html", { "victims": victims, "village":village } )


def tehsil(request, slug=None):
    villages = Villages.objects.filter(tehsil_id=slug).order_by('village_name')
    all = Data.objects.filter(village_id__in=Subquery(villages.values('id'))).order_by('victim_name')
    stats = calculate_stats(all)
    return render(request, "tehsil.html", {
      "villages": villages,
      "stats": stats
      })


def district(request, slug=None):
    villages = Villages.objects.filter(district_id=slug).order_by('village_name')

    # trying to annotate with number of cases per village    
    villages_distinct = Villages.objects.filter(district_id=slug).values('district','tehsil','tehsil_id').distinct()

    all = Data.objects.filter(village_id__in=Subquery(villages.values('id'))).order_by('victim_name')
    stats = calculate_stats(all)
    
    return render(request, "district.html", {
      "villages": villages_distinct,
      "stats": stats
      })


