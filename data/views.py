from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache import cache
from django.contrib import messages
from django.db.models import OuterRef, Subquery, Count, Sum, F, Q, Avg
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


def map(request):
    all = Data.objects.filter(timeline_start__gte='1980-01-01').values('village_id','village_name','timeline_start','timeline_end','victim_disappeared_killed')
    return render(request, "map.html", { "all": all })


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


def detention(request, type=None, name=None):

    district = Villages.objects.filter(id=OuterRef('village_id')).values('district')
    tehsil = Villages.objects.filter(id=OuterRef('village_id')).values('tehsil')
    tehsil_id = Villages.objects.filter(id=OuterRef('village_id')).values('tehsil_id')
    village = Villages.objects.filter(id=OuterRef('village_id')).values('village_name')

    victims = Data.objects.filter(where_victim_detained__detention_facility_type=type, where_victim_detained__facility_name=name)\
      .annotate( village_name_checked=Subquery(village), district=Subquery(district), tehsil=Subquery(tehsil), tehsil_id=Subquery(tehsil_id) )\
      .order_by(F('district').asc(nulls_last=True),'tehsil','victim_name')

    stats = calculate_stats(victims)
    if name is not None and name is None:
        return messages.warning(request,"Detention %s was not found"%id)
    return render(request, "detention.html", { "victims": victims, "facilityname": name, "stats": stats } )


officials = {
  "S0001":"Sumedh Singh [Saini]",
  "S0002":"Mohd. Izhar Alam",
  "S0003":"Suresh	Arora",
  "S0004":"Lok Nath	Angra",
  "S0005":"Swaran	Singh [Ghotna]",
  "S0006":"Ajit Singh	Sandhu",
  "S0007":"Jasminder [Jaswinder]	Singh",
  "S0008":"Gur Iqbal Singh Bhullar",
  "S0009":"Dinkar Gupta",
  "S0010":"Bua Singh",
  "S0011":"Shiv Kumar",
  "S0012":"Sant Kumar",
  "S0013":"Raj Kishan	Bedi",
  "S0014":"Harinder Singh [Chahal]",
  "S0015":"Gurmeet Singh [Pinky]",
}


@register.filter(name='seniorofficial')
def seniorofficial(value):
    return officials.get(value)



def official(request, slug=None):
    name =  officials.get(slug)

    district = Villages.objects.filter(id=OuterRef('village_id')).values('district')
    tehsil = Villages.objects.filter(id=OuterRef('village_id')).values('tehsil')
    tehsil_id = Villages.objects.filter(id=OuterRef('village_id')).values('tehsil_id')
    village = Villages.objects.filter(id=OuterRef('village_id')).values('village_name')

    victims = Data.objects.filter( Q(security_arrest__soa_code=slug) | Q(security_killed__sok_code=slug) )\
      .annotate( village_name_checked=Subquery(village), district=Subquery(district), tehsil=Subquery(tehsil), tehsil_id=Subquery(tehsil_id) )\
      .order_by(F('district').asc(nulls_last=True),'tehsil','victim_name')

    stats = calculate_stats(victims)
    if id is not None and id is None:
        return messages.warning(request,"Year %s was not found"%id)
    return render(request, "securityforce.html", { "victims": victims, "name": name, "stats": stats } )




def securityforce(request, slug=None):

    forcemap = {
      "police" : Q(arrest_security_type_1=1) | Q(killing_securityforcestype_1=1) | Q(so_approached_type_2=1),
      "bsf" : Q(arrest_security_type_2=1) | Q(killing_securityforcestype_2=1) | Q(so_approached_type_3=1),
      "crpf" : Q(arrest_security_type_3=1) | Q(killing_securityforcestype_3=1) | Q(so_approached_type_4=1),
      "army" : Q(arrest_security_type_4=1) | Q(killing_securityforcestype_4=1) | Q(so_approached_type_5=1),
      "cia" : Q(arrest_security_type_5=1) | Q(killing_securityforcestype_5=1) | Q(so_approached_type_6=1),
      "black-cat" : Q(arrest_security_type_6=1) | Q(killing_securityforcestype_6=1) | Q(so_approached_type_7=1),
    }

    unslug = {
      "police": "Punjab Police",
      "bsf": "BSF",
      "crpf": "CRPF",
      "army": "Army",
      "cia": "CIA",
      "black-cat": "Black Cat"
    }

    _query =  forcemap.get(slug)
    name =  unslug.get(slug)
    
    district = Villages.objects.filter(id=OuterRef('village_id')).values('district')
    tehsil = Villages.objects.filter(id=OuterRef('village_id')).values('tehsil')
    tehsil_id = Villages.objects.filter(id=OuterRef('village_id')).values('tehsil_id')
    village = Villages.objects.filter(id=OuterRef('village_id')).values('village_name')

    victims = Data.objects.filter( _query )\
      .annotate( village_name_checked=Subquery(village), district=Subquery(district), tehsil=Subquery(tehsil), tehsil_id=Subquery(tehsil_id) )\
      .order_by(F('district').asc(nulls_last=True),'tehsil','victim_name')

    stats = calculate_stats(victims)
    if id is not None and id is None:
        return messages.warning(request,"Security Force %s was not found"%id)
    return render(request, "securityforce.html", { "victims": victims, "name": name, "stats": stats } )



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

      cache.set("tehsils" + slug, tehsils, 3600) # 60 * 60 seconds
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


