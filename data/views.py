from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache import cache
from django.contrib import messages
from django.db.models import OuterRef, Subquery, Count, Sum, F
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
    district = Villages.objects.filter(id=OuterRef('village_id')).values('district')
    tehsil = Villages.objects.filter(id=OuterRef('village_id')).values('tehsil')
    tehsil_id = Villages.objects.filter(id=OuterRef('village_id')).values('tehsil_id')
    village = Villages.objects.filter(id=OuterRef('village_id')).values('village_name')
    victims = Data.objects.filter(timeline_start__year=year,timeline_end__year=year)\
      .annotate( village_name_checked=Subquery(village), district=Subquery(district), tehsil=Subquery(tehsil), tehsil_id=Subquery(tehsil_id) )\
      .order_by(F('district').asc(nulls_last=True),'tehsil','victim_name')
    stats = calculate_stats(victims)
    if id is not None and id is None:
        return messages.warning(request,"Year %s was not found"%id)
    return render(request, "year.html", { "victims": victims, "year":year, "stats": stats } )



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




def get_tehsils(slug):
    tehsils = cache.get("tehsils" + slug)
    if tehsils:
        return tehsils
    try:
      tehsils = Villages.objects.filter(district_id=slug)\
                        .values('tehsil', 'tehsil_id')\
                        .distinct()
      for tehsil in tehsils:
          datas = Data.objects.filter(village_id=OuterRef('pk'))\
                              .values('village_id')\
                              .annotate(Count('village_id'))\
                              .values('village_id__count')
          villages_data_count = Villages.objects.filter(tehsil_id=tehsil.get('tehsil_id'))\
                                        .values('id')\
                                        .annotate(data_count=Subquery(datas))\
                                        .order_by('-data_count')\
                                        .values('data_count')
          tehsil['data_count'] = villages_data_count.aggregate(Sum('data_count'))\
                                                    .get('data_count__sum')

      cache.set("tehsils" + slug, tehsils, 3600) # 60 * 60 seconds!
      return tehsils

    except Exception as e:
        return messages.warning("Exception get_tehsils:"%e)
        return None



def district(request, slug=None):

#    tehsils = Villages.objects.filter(district_id=slug)\
#                                    .values('tehsil', 'tehsil_id')\
#                                    .distinct()
#    for tehsil in tehsils:
#        datas = Data.objects.filter(village_id=OuterRef('pk'))\
#                            .values('village_id')\
#                            .annotate(Count('village_id'))\
#                            .values('village_id__count')
#        villages_data_count = Villages.objects.filter(tehsil_id=tehsil.get('tehsil_id'))\
#                                        .values('id')\
#                                        .annotate(data_count=Subquery(datas))\
#                                        .order_by('-data_count')\
#                                        .values('data_count')
#        tehsil['data_count'] = villages_data_count.aggregate(Sum('data_count'))\
#                                                    .get('data_count__sum')

    tehsils = get_tehsils(slug)
    villages = Villages.objects.filter(district_id=slug).order_by('village_name')
    district = Villages.objects.filter(district_id=slug)[:1].values('district')
    all = Data.objects.filter(village_id__in=Subquery(villages.values('id'))).order_by('victim_name')
    stats = calculate_stats(all)
    
    return render(request, "district.html", {
      "district": district,
      "villages": tehsils,
      "stats": stats
      })



def page(request, directory=None, slug=None):
    page = Page.objects.get(slug=slug)
    if id is not None and page is None:
        return messages.warning(request,"page %s was not found"%id)
    return render(request, "page.html", { "page":page } )


