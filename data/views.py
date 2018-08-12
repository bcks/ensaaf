from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache import cache
from django.contrib import messages
from django.db.models import OuterRef, Subquery, Count, Sum, F, Q, DateField
from django.db.models.functions import Trunc
from django.template.defaulttags import register

from .models import *
from django.shortcuts import render
from .utils import calculate_stats
from .filters import DataFilter







def home(request):    
    all = Data.objects.all().exclude(victim_name__exact='Anonymous')
    victims = all.order_by('?')[:10]    
    return render(request, "home.html", { 
      "victims": victims
      })


def profiles(request):
    selected_age = request.GET.get('age','')
    selected_caste = request.GET.get('caste','')
    selected_classification = request.GET.get('classification','')
    selected_first_name = request.GET.get('first_name','')
    selected_gender = request.GET.get('gender','')
    selected_militancy = request.GET.get('militancy','')
    selected_religion = request.GET.get('religion','')
    selected_district = request.GET.get('district','')
    selected_tehsil = request.GET.get('tehsil','')
    selected_year = request.GET.get('year','')
    selected_sort = request.GET.get('sort','')

    selected = []
    if selected_age:
      selected.append(selected_age)
    if selected_caste:
      selected.append(selected_caste)
    if selected_district:
      selected.append( get_district_name(selected_district) )
    if selected_classification:
      selected.append(selected_classification)
    if selected_first_name:
      selected.append(selected_first_name)
    if selected_gender:
      selected.append(selected_gender)
    if selected_militancy:
      selected.append(selected_militancy)
    if selected_religion:
      selected.append(selected_religion)
    if selected_tehsil:
      selected.append( get_tehsil_name(selected_tehsil) )
    if selected_year:
      selected.append(selected_year)



    if selected_sort == 'Newest to Oldest':
      victim_list = Data.objects.all().values(\
        'victim_name','victim_disappeared_killed','timeline_start','timeline_end','village_name','photo_vic_fn','record_id')\
        .annotate(year=Trunc('timeline', 'year', output_field=DateField() ))\
        .order_by('-timeline')
      years = list(reversed(range(1981,2008)))
    else:
      victim_list = Data.objects.all().values(\
        'victim_name','victim_disappeared_killed','timeline_start','timeline_end','village_name','photo_vic_fn','record_id')\
        .annotate(year=Trunc('timeline', 'year', output_field=DateField() ))\
        .extra(select={'timeline_is_null': "timeline = '0000-00-00'"}, order_by=['timeline_is_null', 'timeline'])
      years = list(range(1981,2008))

    victim_filter = DataFilter(request.GET, queryset=victim_list)

    years.append('Date Unknown')
    first_names = get_first_names()
    tehsil_list = get_tehsil_list()
    district_list = get_district_list()

    return render(request, "profiles.html", { 
      "victims": victim_filter.qs,
      "years": years,
      "first_names": first_names,
      "tehsil_list": tehsil_list,
      "district_list": district_list,
      'selected_age': selected_age,
      'selected_caste': selected_caste,
      'selected_classification': selected_classification,
      'selected_district': selected_district,
      'selected_first_name': selected_first_name,
      'selected_gender': selected_gender,
      'selected_religion': selected_religion,
      'selected_militancy': selected_militancy,
      'selected_tehsil': selected_tehsil,
      'selected_year': selected_year,
      'selected_sort': selected_sort,
      'selected': selected,
      })


def overview(request):    
    all = Data.objects.all();
    stats = calculate_stats(all)    
    return render(request, "overview.html", { 
      "stats": stats
      })


def map(request):
    selected_age = request.GET.get('age','')
    selected_caste = request.GET.get('caste','')
    selected_classification = request.GET.get('classification','')
    selected_first_name = request.GET.get('first_name','')
    selected_gender = request.GET.get('gender','')
    selected_militancy = request.GET.get('militancy','')
    selected_religion = request.GET.get('religion','')
    selected_district = request.GET.get('district','')
    selected_tehsil = request.GET.get('tehsil','')
    selected_year = request.GET.get('year','')
    selected_urban_rural = request.GET.get('urban_rural','')

    selected = []
    if selected_age:
      selected.append(selected_age)
    if selected_caste:
      selected.append(selected_caste)
    if selected_district:
      selected.append( get_district_name(selected_district) )
    if selected_classification:
      selected.append(selected_classification)
    if selected_first_name:
      selected.append(selected_first_name)
    if selected_gender:
      selected.append(selected_gender)
    if selected_militancy:
      selected.append(selected_militancy)
    if selected_religion:
      selected.append(selected_religion)
    if selected_tehsil:
      selected.append( get_tehsil_name(selected_tehsil) )
    if selected_year:
      selected.append(selected_year)
    if selected_urban_rural:
      selected.append(selected_urban_rural)
      
    victim_list = Data.objects.filter(timeline__gte='1980-01-01',timeline__lte='2000-12-31').values('village_id','village_name','timeline')
    victim_filter = DataFilter(request.GET, queryset=victim_list)

    years = list(range(1981,2008))
    years.append('Date Unknown')

    first_names = get_first_names()
    tehsil_list = get_tehsil_list()
    district_list = get_district_list()

    return render(request, "map.html", { 
      "all": victim_filter.qs,
      "years": years,
      "first_names": first_names,
      "tehsil_list": tehsil_list,
      "district_list": district_list,
      'selected_age': selected_age,
      'selected_caste': selected_caste,
      'selected_classification': selected_classification,
      'selected_district': selected_district,
      'selected_first_name': selected_first_name,
      'selected_gender': selected_gender,
      'selected_religion': selected_religion,
      'selected_militancy': selected_militancy,
      'selected_tehsil': selected_tehsil,
      'selected_year': selected_year,
      'selected': selected,
      })


def map_ajax(request):
    victim_list = Data.objects.filter(timeline__gte='1980-01-01',timeline__lte='2000-12-31').values('village_id','village_name','timeline')    
    victim_filter = DataFilter(request.GET, queryset=victim_list)
    return render(request, "map_ajax.html", { "all": victim_filter.qs, }, content_type='application/json')

def change(request):
    return render(request, "change.html")


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

    soas = SecurityArrest.objects.filter(soa_code=slug).values_list('record_id', flat=True)
    soks = SecurityKilled.objects.filter(sok_code=slug).values_list('record_id', flat=True)
    records = list(soas) + list(soks)
        
    victims = Data.objects.filter( record_id__in=records )\
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
      "cia": "Criminal Investigation Agency",
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



def get_first_names():
    first_names = cache.get("first_names")
    if first_names:
        return first_names
    try:
      first_names = Data.objects.all()\
                        .values('victim_first_name')\
                        .distinct().order_by('victim_first_name')
      cache.set("first_names", first_names, 3600) # 60 * 60 seconds
      return first_names
    except Exception as e:
        return messages.warning("Exception get_first_names:"%e)
        return None
        


def get_tehsil_list():
    tehsil_list = cache.get("tehsil_list")
    if tehsil_list:
        return tehsil_list
    try:
      tehsil_list = Villages.objects.all()\
                        .values('tehsil', 'tehsil_id')\
                        .distinct().order_by('tehsil')
      cache.set("tehsil_list", tehsil_list, 3600) # 60 * 60 seconds
      return tehsil_list
    except Exception as e:
        return messages.warning("Exception get_tehsil_list:"%e)
        return None
     
def get_district_list():
    district_list = cache.get("district_list")
    if district_list:
        return district_list
    try:
      district_list = Villages.objects.all()\
                        .values('district', 'district_id')\
                        .distinct().order_by('district')
      cache.set("district_list", district_list, 3600) # 60 * 60 seconds
      return district_list
    except Exception as e:
        return messages.warning("Exception get_district_list:"%e)
        return None
     

def get_tehsil_name(value):
    if value:
      tehsil_name = Villages.objects.filter(tehsil_id=value).values('tehsil')[:1].get()
      return tehsil_name['tehsil']
    else:
      return None

def get_district_name(value):
    if value:
      district_name = Villages.objects.filter(district_id=value).values('district')[:1].get()
      return district_name['district']
    else:
      return None


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


