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


def overview(request):    
    all = Data.objects.all();
    stats = calculate_stats(all)    
    return render(request, "overview.html", { 
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


def year(request, year=None):

    tehsil = Villages.objects.filter(id=OuterRef('village_id')).values('tehsil')
    tehsil_id = Villages.objects.filter(id=OuterRef('village_id')).values('tehsil_id')
    village = Villages.objects.filter(id=OuterRef('village_id')).values('village_name')
    victims = Data.objects.filter(timeline_start__year=year,timeline_end__year=year)\
      .annotate(village_name_checked=Subquery(village), tehsil=Subquery(tehsil), tehsil_id=Subquery(tehsil_id))\
      .order_by('tehsil','village_name','victim_name')

#    victims = Data.objects.filter(timeline_start__year=year,timeline_end__year=year).order_by('victim_name')

    stats = calculate_stats(victims)
    if id is not None and id is None:
        return messages.warning(request,"Year %s was not found"%id)
    return render(request, "year.html", { "victims": victims, "year":year, "stats": stats } )



def securityarrest(request, id=None):
    security_arrest = SecurityArrest.objects.filter(id=id)[:1].get()

    security_arrest_victims = SecurityArrest.objects.filter(
      arrest_so_first_name=security_arrest.arrest_so_first_name,
      arrest_so_last_name=security_arrest.arrest_so_last_name,
      arrest_so_rank=security_arrest.arrest_so_rank,
      arrest_so_affiliation=security_arrest.arrest_so_affiliation,
      ).values('record_id')

    security_killed_victims = SecurityKilled.objects.filter(
      killing_so_first_name=security_arrest.arrest_so_first_name,
      killing_so_last_name=security_arrest.arrest_so_last_name,
      killing_so_rank=security_arrest.arrest_so_rank,
      killing_so_affiliation=security_arrest.arrest_so_affiliation,
      ).values('record_id')
      
    victims_arrest = Data.objects.filter(record_id__in=security_arrest_victims).order_by('victim_name')
    victims_killed = Data.objects.filter(record_id__in=security_killed_victims).order_by('victim_name')
    
    victims = victims_arrest | victims_killed

    stats = calculate_stats(victims)
    if id is not None and id is None:
        return messages.warning(request,"Year %s was not found"%id)
    return render(request, "security.html", { "victims": victims, "stats": stats } )


def securitykilled(request, id=None):
    security_killed = SecurityKilled.objects.filter(id=id)[:1].get()

    security_arrest_victims = SecurityArrest.objects.filter(
      arrest_so_first_name=security_killed.killing_so_first_name,
      arrest_so_last_name=security_killed.killing_so_last_name,
      arrest_so_rank=security_killed.killing_so_rank,
      arrest_so_affiliation=security_killed.killing_so_affiliation,
      ).values('record_id')

    security_killed_victims = SecurityKilled.objects.filter(
      killing_so_first_name=security_killed.killing_so_first_name,
      killing_so_last_name=security_killed.killing_so_last_name,
      killing_so_rank=security_killed.killing_so_rank,
      killing_so_affiliation=security_killed.killing_so_affiliation,
      ).values('record_id')
                
    victims_arrest = Data.objects.filter(record_id__in=security_arrest_victims).order_by('victim_name')
    victims_killed = Data.objects.filter(record_id__in=security_killed_victims).order_by('victim_name')
    
    victims = victims_arrest | victims_killed

    stats = calculate_stats(victims)
    if id is not None and id is None:
        return messages.warning(request,"Year %s was not found"%id)
    return render(request, "security.html", { "victims": victims, "stats": stats } )



def tehsil(request, slug=None):
    datas = Data.objects.filter(village_id=OuterRef('pk'))\
                            .values('village_id')\
                            .annotate(Count('village_id'))\
                            .values('village_id__count')    

    villages_with_count = Villages.objects.filter(tehsil_id=slug)\
                                  .annotate(data_count=Subquery(datas))\
                                  .exclude(data_count=None).order_by('-data_count','village_name')

    villages = Villages.objects.filter(tehsil_id=slug).values('id','district','district_id','tehsil')

    all = Data.objects.filter(village_id__in=Subquery(villages.values('id'))).order_by('victim_name')
    stats = calculate_stats(all)
    return render(request, "tehsil.html", {
      'villages_with_count': villages_with_count,
      'villages': villages,
      "stats": stats
      })


def district(request, slug=None):

    # Single query approach - slower
    # datas = Data.objects.filter(village_id=OuterRef('pk'))\
    #                 .values('village_id')\
    #                 .annotate(Count('village_id'))\
    #                 .values('village_id__count')
    # villages_data_count = Villages.objects.filter(tehsil_id=OuterRef('tehsil_id'))\
    #                                 .annotate(data_count=Subquery(datas))\
    #                                 .order_by('-data_count')\
    #                                 .values('data_count')[:1]
    # tehsils = Villages.objects.filter(district_id=slug)\
    #                             .annotate(data_count=Subquery(villages_data_count))\
    #                             .values('tehsil', 'tehsil_id', 'data_count')\
    #                             .distinct()

    # Multiple queries approach - faster
    tehsils = list(Villages.objects.filter(district_id=slug)\
                                .values('tehsil', 'tehsil_id', 'district')\
                                .distinct())
    for tehsil in tehsils:
        datas = Data.objects.filter(village_id=OuterRef('pk'))\
                        .values('village_id')\
                        .annotate(Count('village_id'))\
                        .values('village_id__count')
        villages_data_count = Villages.objects.filter(tehsil_id=tehsil.get('tehsil_id'))\
                                        .annotate(data_count=Subquery(datas))\
                                        .order_by('-data_count')\
                                        .values('data_count')[:1]
        tehsil['data_count'] = villages_data_count.first().get('data_count')

    villages = Villages.objects.filter(district_id=slug).order_by('village_name')
    all = Data.objects.filter(village_id__in=Subquery(villages.values('id'))).order_by('victim_name')
    stats = calculate_stats(all)
    
    return render(request, "district.html", {
      "villages": tehsils,
      "stats": stats
      })




def page(request, directory=None, slug=None):
    page = Page.objects.get(slug=slug)
    if id is not None and page is None:
        return messages.warning(request,"page %s was not found"%id)
    return render(request, "page.html", { "page":page } )


