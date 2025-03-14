import os
import re
import operator
from functools import reduce

from django.shortcuts import render
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache import cache
from django.contrib import messages
from django.db.models import OuterRef, Subquery, Count, Sum, F, Q, DateField
from django.db.models.functions import Trunc
from django.http import Http404
from django.template.defaulttags import register
from django.template.loader import render_to_string
from django.views.decorators.cache import cache_page
from django.urls import reverse
from django.utils.translation import gettext as _
from django.utils.translation import get_language

from .models import *
from django.shortcuts import render, redirect
from .utils import calculate_stats
from .filters import DataFilter

# contact form
from django.conf import settings
from .forms import ContactForm
from django.core.mail import EmailMessage

# autocomplete
import simplejson as json
from django.http import HttpResponse
from haystack.query import SearchQuerySet

# spelling suggestions
import pysolr
solr = pysolr.Solr(settings.HAYSTACK_CONNECTIONS['default']['URL'], timeout=10)


from interviews.models import Victim



tehsils_for_translation = [ _("Ajnala"), _("Amritsar I"), _("Amritsar II"), _("Baba Bakala"), _("Khadoor Sahib"), _("Patti"), _("Tarn Taran"), _("Rampura Phul"), _("Talwandi Sabo"), _("Jaitu"), _("Amloh"), _("Bassi Pathana"), _("Khamanon"), _("Abohar"), _("Fazilka"), _("Jalalabad"), _("Zira"), _("Batala"), _("Dera Baba Nanak"), _("Dhar Kalan"), _("Pathankot"), _("Dasuya"), _("Garhshankar"), _("Mukerian"), _("Jalandhar I"), _("Jalandhar II"), _("Nakodar"), _("Phillaur"), _("Shahkot"), _("Bhulath"), _("Phagwara"), _("Sultanpur Lodhi"), _("Jagroan"), _("Khanna"), _("Ludhiana East"), _("Ludhiana West"), _("Payal"), _("Raikot"), _("Samrala"), _("Budhlada"), _("Sardulgarh"), _("Bhagha Purana"), _("Nihal Singhwala"), _("Giddarbaha"), _("Malout"), _("Balachaur"), _("Dera Bassi"), _("Nabha"), _("Rajpura"), _("Samana"), _("Anandpur Sahib"), _("Kharar"), _("S.A.S.Nagar (Mohali)"), _("Barnala"), _("Dhuri"), _("Malerkotla"), _("Moonak"), _("Sunam") ]

unknown_for_translation = _("unknown")

districts = [{"district":"Amritsar","district_pb":"ਅੰਮ੍ਰਿਤਸਰ","district_id":302,"subdistricts":[{"tehsil":"Ajnala","tehsil_pb":"ਅਜਨਾਲਾ","tehsil_id":3020001},{"tehsil":"Amritsar I","tehsil_pb":"ਅੰਮ੍ਰਿਤਸਰ - I","tehsil_id":3020002},{"tehsil":"Amritsar II","tehsil_pb":"ਅੰਮ੍ਰਿਤਸਰ - II","tehsil_id":3020003},{"tehsil":"Baba Bakala","tehsil_pb":"ਬਾਬਾ ਬਕਾਲਾ","tehsil_id":3020007},{"tehsil":"Khadoor Sahib","tehsil_pb":"ਖਡੂਰ ਸਾਹਿਬ","tehsil_id":3020006},{"tehsil":"Patti","tehsil_pb":"ਪੱਟੀ","tehsil_id":3020005},{"tehsil":"Tarn Taran","tehsil_pb":"ਤਰਨ ਤਾਰਨ","tehsil_id":3020004}]},{"district":"Bathinda","district_pb":"ਬਠਿੰਡਾ","district_id":314,"subdistricts":[{"tehsil":"Bathinda","tehsil_pb":"ਬਠਿੰਡਾ","tehsil_id":3140002},{"tehsil":"Rampura Phul","tehsil_pb":"ਰਾਮਪੁਰਾ ਫੂਲ","tehsil_id":3140001},{"tehsil":"Talwandi Sabo","tehsil_pb":"ਤਲਵੰਡੀ ਸਾਬੋ","tehsil_id":3140003}]},{"district":"Faridkot","district_pb":"ਫਰੀਦਕੋਟ","district_id":313,"subdistricts":[{"tehsil":"Faridkot","tehsil_pb":"ਫਰੀਦਕੋਟ","tehsil_id":3130001},{"tehsil":"Jaitu","tehsil_pb":"ਜੈਤੋ","tehsil_id":3130002}]},{"district":"Fatehgarh Sahib","district_pb":"ਫਤਿਹਗੜ੍ਹ ਸਾਹਿਬ","district_id":308,"subdistricts":[{"tehsil":"Amloh","tehsil_pb":"ਅਮਲੋਹ","tehsil_id":3080003},{"tehsil":"Bassi Pathana","tehsil_pb":"ਬੱਸੀ ਪਠਾਣਾਂ","tehsil_id":3080001},{"tehsil":"Fatehgarh Sahib","tehsil_pb":"ਫਤਿਹਗੜ੍ਹ ਸਾਹਿਬ","tehsil_id":3080002},{"tehsil":"Khamanon","tehsil_pb":"ਖਮਾਣੋ","tehsil_id":3080004}]},{"district":"Firozpur","district_pb":"ਫਿਰੋਜਪੁਰ","district_id":311,"subdistricts":[{"tehsil":"Abohar","tehsil_pb":"ਅਬੋਹਰ","tehsil_id":3110005},{"tehsil":"Fazilka","tehsil_pb":"ਫਾਜ਼ਿਲਕਾ","tehsil_id":3110004},{"tehsil":"Firozpur","tehsil_pb":"ਫਿਰੋਜਪੁਰ","tehsil_id":3110002},{"tehsil":"Jalalabad","tehsil_pb":"ਜਲਾਲਾਬਾਦ","tehsil_id":3110003},{"tehsil":"Zira","tehsil_pb":"ਜ਼ੀਰਾ","tehsil_id":3110001}]},{"district":"Gurdaspur","district_pb":"ਗੁਰਦਾਸਪੁਰ","district_id":301,"subdistricts":[{"tehsil":"Batala","tehsil_pb":"ਬਟਾਲਾ","tehsil_id":3010004},{"tehsil":"Dera Baba Nanak","tehsil_pb":"ਡੇਰਾ ਬਾਬਾ ਨਾਨਕ","tehsil_id":3010005},{"tehsil":"Dhar Kalan","tehsil_pb":"ਧਾਰ ਕਲਾਂ","tehsil_id":3010001},{"tehsil":"Gurdaspur","tehsil_pb":"ਗੁਰਦਾਸਪੁਰ","tehsil_id":3010003},{"tehsil":"Pathankot","tehsil_pb":"ਪਠਾਨਕੋਟ","tehsil_id":3010002}]},{"district":"Hoshiarpur","district_pb":"ਹੁਸ਼ਿਆਰਪੁਰ","district_id":305,"subdistricts":[{"tehsil":"Dasuya","tehsil_pb":"ਦਸੂਹਾ","tehsil_id":3050001},{"tehsil":"Garhshankar","tehsil_pb":"ਗੜਸ਼ੰਕਰ","tehsil_id":3050004},{"tehsil":"Hoshiarpur","tehsil_pb":"ਹੁਸ਼ਿਆਰਪੁਰ","tehsil_id":3050003},{"tehsil":"Mukerian","tehsil_pb":"ਮੁਕੇਰੀਆਂ","tehsil_id":3050002}]},{"district":"Jalandhar","district_pb":"ਜਲੰਧਰ","district_id":304,"subdistricts":[{"tehsil":"Jalandhar I","tehsil_pb":"ਜਲੰਧਰ - I","tehsil_id":3040004},{"tehsil":"Jalandhar II","tehsil_pb":"ਜਲੰਧਰ - II","tehsil_id":3040005},{"tehsil":"Nakodar","tehsil_pb":"ਨਕੋਦਰ","tehsil_id":3040002},{"tehsil":"Phillaur","tehsil_pb":"ਫਿਲੌਰ","tehsil_id":3040003},{"tehsil":"Shahkot","tehsil_pb":"ਸ਼ਾਹਕੋਟ","tehsil_id":3040001}]},{"district":"Kapurthala","district_pb":"ਕਪੂਰਥਲਾ","district_id":303,"subdistricts":[{"tehsil":"Bhulath","tehsil_pb":"ਭੁਲੱਥ","tehsil_id":3030001},{"tehsil":"Kapurthala","tehsil_pb":"ਕਪੂਰਥਲਾ","tehsil_id":3030002},{"tehsil":"Phagwara","tehsil_pb":"ਫੱਗਵਾੜਾ","tehsil_id":3030004},{"tehsil":"Sultanpur Lodhi","tehsil_pb":"ਸੁਲਤਾਨਪੁਰ ਲੋਧੀ","tehsil_id":3030003}]},{"district":"Ludhiana","district_pb":"ਲੁਧਿਆਣਾ","district_id":309,"subdistricts":[{"tehsil":"Jagraon","tehsil_pb":"ਜਗਰਾਓ","tehsil_id":3090007},{"tehsil":"Khanna","tehsil_pb":"ਖੰਨਾ","tehsil_id":3090002},{"tehsil":"Ludhiana East","tehsil_pb":"ਲੁਧਿਆਣਾ ਈਸਟ","tehsil_id":3090004},{"tehsil":"Ludhiana West","tehsil_pb":"ਲੁਧਿਆਣਾ ਵੈਸਟ","tehsil_id":3090005},{"tehsil":"Payal","tehsil_pb":"ਪਾਇਲ","tehsil_id":3090003},{"tehsil":"Raikot","tehsil_pb":"ਰਾਏਕੋਟ","tehsil_id":3090006},{"tehsil":"Samrala","tehsil_pb":"ਸਮਰਾਲਾ","tehsil_id":3090001}]},{"district":"Mansa","district_pb":"ਮਾਨਸਾ","district_id":315,"subdistricts":[{"tehsil":"Budhlada","tehsil_pb":"ਬੁੱਡਲਾਡਾ","tehsil_id":3150002},{"tehsil":"Mansa","tehsil_pb":"ਮਾਨਸਾ","tehsil_id":3150003},{"tehsil":"Sardulgarh","tehsil_pb":"ਸਰਦੂਲਗੱੜ","tehsil_id":3150001}]},{"district":"Moga","district_pb":"ਮੋਗਾ","district_id":310,"subdistricts":[{"tehsil":"Bhagha Purana","tehsil_pb":"ਬਾਘਾ ਪੁਰਾਣਾ","tehsil_id":3100002},{"tehsil":"Moga","tehsil_pb":"ਮੋਗਾ","tehsil_id":3100003},{"tehsil":"Nihal Singhwala","tehsil_pb":"ਨਿਹਾਲ ਸਿੰਘਵਾਲਾ","tehsil_id":3100001}]},{"district":"Muktsar","district_pb":"ਮੁਕਤਸਰ","district_id":312,"subdistricts":[{"tehsil":"Giddarbaha","tehsil_pb":"ਗਿੱਦੜਬਾਹਾ","tehsil_id":3120002},{"tehsil":"Malout","tehsil_pb":"ਮਲੋਟ","tehsil_id":3120001},{"tehsil":"Muktsar","tehsil_pb":"ਮੁਕਤਸਰ","tehsil_id":3120003}]},{"district":"Nawanshahr","district_pb":"ਨਵਾਂਸ਼ਹਿਰ","district_id":306,"subdistricts":[{"tehsil":"Balachaur","tehsil_pb":"ਬਲਾਚੌਰ","tehsil_id":3060002},{"tehsil":"Nawanshahr","tehsil_pb":"ਨਵਾਂਸ਼ਹਿਰ","tehsil_id":3060001}]},{"district":"Patiala","district_pb":"ਪਟਿਆਲਾ","district_id":317,"subdistricts":[{"tehsil":"Dera Bassi","tehsil_pb":"ਡੇਰਾ ਬੱਸੀ","tehsil_id":3170005},{"tehsil":"Nabha","tehsil_pb":"ਨਾਭਾ","tehsil_id":3170002},{"tehsil":"Patiala","tehsil_pb":"ਪਟਿਆਲਾ","tehsil_id":3170003},{"tehsil":"Rajpura","tehsil_pb":"ਰਾਜਪੁਰਾ","tehsil_id":3170004},{"tehsil":"Samana","tehsil_pb":"ਸਮਾਣਾ","tehsil_id":3170001}]},{"district":"Rupnagar","district_pb":"ਰੂਪਨਗਰ","district_id":307,"subdistricts":[{"tehsil":"Anandpur Sahib","tehsil_pb":"ਅਨੰਦਪੁਰ ਸਾਹਿਬ","tehsil_id":3070001},{"tehsil":"Kharar","tehsil_pb":"ਖਰੜ","tehsil_id":3070003},{"tehsil":"Rupnagar","tehsil_pb":"ਰੂਪਨਗਰ","tehsil_id":3070002},{"tehsil":"S.A.S.Nagar (Mohali)","tehsil_pb":"ਸਾਹਿਬਜ਼ਾਦਾ ਅਜੀਤ ਸਿੰਘ ਨਗਰ (ਮੋਹਾਲੀ)","tehsil_id":3070004}]},{"district":"Sangrur","district_pb":"ਸੰਗਰੂਰ","district_id":316,"subdistricts":[{"tehsil":"Barnala","tehsil_pb":"ਬਰਨਾਲਾ","tehsil_id":3160001},{"tehsil":"Dhuri","tehsil_pb":"ਧੂਰੀ","tehsil_id":3160003},{"tehsil":"Malerkotla","tehsil_pb":"ਮਲੇਰਕੋਟਲਾ","tehsil_id":3160002},{"tehsil":"Moonak","tehsil_pb":"ਮੂਨਕ","tehsil_id":3160006},{"tehsil":"Sangrur","tehsil_pb":"ਸੰਗਰੂਰ","tehsil_id":3160004},{"tehsil":"Sunam","tehsil_pb":"ਸੁਨਾਮ","tehsil_id":3160005}]}]



@register.simple_tag()
def lang():
  if get_language() == 'pb':
    return '/pb'
  else:
    return ''


@cache_page(60 * 60)
def profiles(request):
    selected_age = request.GET.get('age','')
    selected_caste = request.GET.get('caste','')
    selected_classification = request.GET.get('classification','')
    selected_first_name = request.GET.get('first_name','')
    selected_gender = request.GET.get('gender','')
    selected_urban_rural = request.GET.get('urban_rural','')
    selected_combatant = request.GET.get('combatant','')
    selected_religion = request.GET.get('religion','')
    selected_district = request.GET.get('district','')
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
    if selected_urban_rural:
      selected.append(selected_urban_rural)
    if selected_combatant:
      selected.append(selected_combatant)
    if selected_religion:
      selected.append(selected_religion)
    if selected_year:
      selected.append(selected_year)


    if selected_sort == 'Newest to Oldest':
      victim_list = Data.objects.all().values(\
        'victim_name','victim_name_pb','victim_disappeared_killed','timeline_start','timeline_end','village_name','village_name_pb','photo_vic_fn','record_id','victim_sex')\
        .annotate(year=Trunc('timeline', 'year', output_field=DateField() ))\
        .order_by('-timeline')
      years = list(reversed(range(1981,2008)))
      years.insert(0, 2012)
    else:
      victim_list = Data.objects.all().values(\
        'victim_name','victim_name_pb','victim_disappeared_killed','timeline_start','timeline_end','village_name','village_name_pb','photo_vic_fn','record_id','victim_sex')\
        .annotate(year=Trunc('timeline', 'year', output_field=DateField() ))\
        .extra(select={'timeline_is_null': "timeline = '0000-00-00'"}, order_by=['-timeline_is_null', 'timeline'])
      years = list(range(1981,2008))
      years.append(2012)

    victim_filter = DataFilter(request.GET, queryset=victim_list)

    years.append( 'Date Unknown' )

    first_names = get_first_names()

    return render(request, "profiles.html", { 
      "victims": victim_filter.qs,
      "years": years,
      "first_names": first_names,
      "districts": districts,
      'selected_age': selected_age,
      'selected_caste': selected_caste,
      'selected_classification': selected_classification,
      'selected_district': selected_district,
      'selected_first_name': selected_first_name,
      'selected_gender': selected_gender,
      'selected_urban_rural': selected_urban_rural,
      'selected_religion': selected_religion,
      'selected_combatant': selected_combatant,
      'selected_year': selected_year,
      'selected_sort': selected_sort,
      'selected': selected,
      })


@cache_page(60 * 60)
def overview(request):    
    all = Data.objects.all();
    stats = calculate_stats(all)    
    return render(request, "overview.html", { 
      "stats": stats
      })


@cache_page(60 * 60)
def detail(request):    
    return render(request, "detail.html")


@cache_page(60 * 60)
def map(request):
    selected_age = request.GET.get('age','')
    selected_caste = request.GET.get('caste','')
    selected_classification = request.GET.get('classification','')
    selected_gender = request.GET.get('gender','')
    selected_urban_rural = request.GET.get('urban_rural','')
    selected_combatant = request.GET.get('combatant','')
    selected_religion = request.GET.get('religion','')
    selected_district = request.GET.get('district','')
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
    if selected_gender:
      selected.append(selected_gender)
    if selected_urban_rural:
      selected.append(selected_urban_rural)
    if selected_combatant:
      selected.append(selected_combatant)
    if selected_religion:
      selected.append(selected_religion)
    if selected_year:
      selected.append(selected_year)
    if selected_urban_rural:
      selected.append(selected_urban_rural)

    victim_list = Data.objects.values('village_id','village_name','village_name','timeline')
    total = victim_list.count()

    years = list(range(1981,2008))
    years.append(2012)
    years.append('Date Unknown')

    return render(request, "map.html", { 
      "total": total,
      "all": victim_list,
      "years": years,
      "districts": districts,
      'selected_age': selected_age,
      'selected_caste': selected_caste,
      'selected_classification': selected_classification,
      'selected_district': selected_district,
      'selected_gender': selected_gender,
      'selected_urban_rural': selected_urban_rural,
      'selected_religion': selected_religion,
      'selected_combatant': selected_combatant,
      'selected_year': selected_year,
      'selected_urban_rural': selected_urban_rural,
      'selected': selected,
      })


@cache_page(60 * 60)
def map_ajax(request):
    victim_list = Data.objects.values('village_id','village_name','timeline')    
    victim_filter = DataFilter(request.GET, queryset=victim_list)
    return render(request, "map_ajax.html", { "all": victim_filter.qs, }, content_type='application/json')


def change(request):
    return render(request, "change.html")



def random_photos(request, record_id=None):
    male_child = Data.objects.filter(photo_vic_fn__isnull=False,victim_age__lt=18,victim_sex='1').order_by('?')[:1]
    female_child = Data.objects.filter(photo_vic_fn__isnull=False,victim_age__lt=18,victim_sex='2').order_by('?')[:1]
    female_elderly = Data.objects.filter(photo_vic_fn__isnull=False,victim_age__gt=60,victim_sex='2').order_by('?')[:1]
    male_elderly = Data.objects.filter(photo_vic_fn__isnull=False,victim_age__gt=60,victim_sex='1').order_by('?')[:1]
    randoms = Data.objects.filter(photo_vic_fn__isnull=False).order_by('?')[:96]
    result_list = randoms.union(male_child,female_child,male_elderly,female_elderly)
    return render(request, "100photos.html", { "victims": result_list }, content_type="text/csv")


# one female child victim
# one female elderly victim
# one male child victm
# one male elderly victim 
      



@cache_page(60 * 60)
def profile(request, record_id=None):
    try:
      queryset = Data.objects.filter(record_id=record_id)
      victim = queryset[:1].get()
    except Exception as e:
        raise Http404("Profile was not found")

    if victim.village_id:
      try:
        village = Villages.objects.filter(vid=victim.village_id)[:1].get()
      except Villages.DoesNotExist:
        village = None
    else:
      village = None
    if record_id is not None and victim is None:
        return messages.warning(request,"Profile %s was not found"%record_id)

    interviews = Victim.objects.filter(profile_id=record_id)

    return render(request, "profile.html", {
      "victim": victim,
      "village": village,
      "interviews": interviews
    })



def tweet(request, record_id=None):
    try:
      queryset = Data.objects.filter(record_id=record_id)
      victim = queryset[:1].get()
    except Exception as e:
        raise Http404("Profile was not found")

    if victim.village_id:
      try:
        village = Villages.objects.filter(vid=victim.village_id)[:1].get()
      except Villages.DoesNotExist:
        village = None
    else:
      village = None
    if record_id is not None and victim is None:
        return messages.warning(request,"Profile %s was not found"%record_id)

    return render(request, "tweet/tweet.html", {
      "victim": victim,
      "village": village,
    })


def tweets(request):
    victims = Data.objects.all()
    return render(request, "tweet/tweets.html", {
      "victims": victims,
    })

def tweetsdate(request, year=None, month=None, date=None):
    victims = Data.objects.filter(timeline__month=month,timeline__day=date)
    return render(request, "tweet/tweetsdate.html", {
      "victims": victims,
    })


def all_profiles(request, slug=0):
    start = int(slug) * 500
    end = start + 500
    victims = Data.objects.all()[start:end]
    return render(request, "all_profiles.html", {
      "victims": victims,
    })



@cache_page(60 * 60)
def village(request, slug=None):

    victim_list = Data.objects.filter(village_id=slug).order_by('victim_name')
    victim_filter = DataFilter(request.GET, queryset=victim_list)
    total_victims = victim_list.count()
    
    village = Villages.objects.filter(vid=slug)[:1].get()

    if slug is not None and slug is None:
        return messages.warning(request,"Village %s was not found"%slug)
    return render(request, "village.html", { "vid": slug, "total_victims": total_victims, "victims": victim_filter, "village":village } )


@cache_page(60 * 60)
def year(request, year=None):
    district = Villages.objects.filter(vid=OuterRef('village_id')).values('district')
    tehsil = Villages.objects.filter(vid=OuterRef('village_id')).values('tehsil')
    tehsil_id = Villages.objects.filter(vid=OuterRef('village_id')).values('tehsil_id')
    village = Villages.objects.filter(vid=OuterRef('village_id')).values('village_name')
    start = year + '-01-01'
    end = year + '-12-31'

    # SELECT * FROM data WHERE NOT (timeline_start > end OR timeline_end < start)
    victims = Data.objects.filter( ~Q(timeline_start__gt=end), ~Q(timeline_end__lt=start) )\
      .annotate( village_name_checked=Subquery(village), district=Subquery(district), tehsil=Subquery(tehsil), tehsil_id=Subquery(tehsil_id) )\
      .order_by(F('district').asc(nulls_last=True),'tehsil','victim_name')
    stats = calculate_stats(victims)
    if year is not None and year is None:
        return messages.warning(request,"Year %s was not found"%year)
    return render(request, "year.html", { "victims": victims, "year":year, "stats": stats } )




def villages_cache(request):
    datas = Data.objects.filter(village_id=OuterRef('pk'))\
                            .values('village_id')\
                            .annotate(Count('village_id'))\
                            .values('village_id__count')    
    
    if get_language() == 'pb':
      villages = Villages.objects.all().values('village_name_pb','vid','district','district_id')\
        .annotate(data_count=Subquery(datas))\
        .order_by('district','village_name_pb')
    else:
      villages = Villages.objects.all().values('village_name','vid','district','district_id')\
        .annotate(data_count=Subquery(datas))\
        .order_by('district','village_name')

    output = render_to_string("villages.html", { "villages": villages }, request)
    
    current_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(current_dir, 'templates/villages_cached_' + get_language() + '.html')
    f=open(file_path,'w+')
    f.write( output ) 
    f.close()
    return HttpResponse('<h1>Villages page is cached</h1>')


#@cache_page(60 * 60 * 365) # cache for a year
def villages(request):
    if get_language() == 'pb':
      return render(request, "villages_cached_pb.html")
    else:
      return render(request, "villages_cached_en-us.html")


@cache_page(60 * 60)
def detention(request, type=None, name=None):
    district = Villages.objects.filter(vid=OuterRef('village_id')).values('district')
    tehsil = Villages.objects.filter(vid=OuterRef('village_id')).values('tehsil')
    tehsil_id = Villages.objects.filter(vid=OuterRef('village_id')).values('tehsil_id')
    village = Villages.objects.filter(vid=OuterRef('village_id')).values('village_name')

    victims = Data.objects.filter(where_victim_detained__detention_facility_type=type, where_victim_detained__facility_name=name)\
      .annotate( village_name_checked=Subquery(village), district=Subquery(district), tehsil=Subquery(tehsil), tehsil_id=Subquery(tehsil_id) )\
      .order_by(F('district').asc(nulls_last=True),'tehsil','victim_name')

    stats = calculate_stats(victims)
    if name is not None and name is None:
        return messages.warning(request,"Detention %s was not found"%name)
    return render(request, "detention.html", { "victims": victims, "facilityname": name, "stats": stats } )


officials = {
  "S0001":_("Sumedh Singh [Saini]"),
  "S0002":_("Mohd. Izhar Alam"),
  "S0003":_("Suresh Arora"),
  "S0004":_("Lok Nath Angra"),
  "S0005":_("Swaran Singh [Ghotna]"),
  "S0006":_("Ajit Singh Sandhu"),
  "S0007":_("Jasminder [Jaswinder] Singh"),
  "S0008":_("Gur Iqbal Singh Bhullar"),
  "S0009":_("Dinkar Gupta"),
  "S0010":_("Des Raj"),
  "S0011":_("Shiv Kumar"),
  "S0012":_("Sant Kumar"),
  "S0013":_("Raj Kishan Bedi"),
  "S0014":_("Harinder Singh [Chahal]"),
  "S0015":_("Gurmeet Singh [Pinky]"),
  "S0016":_("D.R. Bhatti"),
  "S0017":_("Mohd. Mustafa"),
  "S0018":_("Satish Kumar Sharma"),
  "S0019":_("Harkishan Singh Kahlon"),
  "S0020":_("Gobind Ram"),
  "S0021":_("Anil Kumar Sharma"),
  "S0023":_("M.K. Tiwari"),
  "S0024":_("Samant Kumar Goel"),
  "S0026":_("J.P. Birdi"),
  "S0027":_("A.P. Pandey"),
  "S0028":_("Sita Ram"),
  "S0030":_("Sanjiv Gupta"),
  "S0031":_("Khubi Ram"),
  "S0032":_("Sidharth Chattopadhyaya"),
  "S0033":_("C.S.R. Reddy"),
  "S0034":_("Narinderpal Singh"),
  "S0035":_("P.S. Bhinder"),
  "S0036":_("Ajaypal Singh Mann"),
  "S0037":_("Rajinder Singh"),
  "S0038":_("R.S. Chalia"),
  "S0039":_("Bua Singh"),
  "S0040":_("D.S. Mangat"),
  "S0041":_("D.S. Mohi"),
  "S0042":_("N.P.S. Aulakh"),
  "S0043":_("P.S. [Paramjit Singh] Sandhu"),
  "S0044":_("A.S. Bajwa"),
  "S0045":_("S.V. Singh"),
  "S0046":_("Harjit Singh Randhawa"),
  "S0047":_("Sital Das"),
  "S0048":_("P.S. Hura"),
  "S0049":_("M.S. Bhullar"),
  "S0050":_("K.P.S. Gill"),
  "S0051":_("Baldev Singh"),
  "S0052":_("H.R. Banga"),
  "S0053":_("Surjit Singh"),
  "S0054":_("Hardeep Dhillon"),
  "S0055":_("Arpit Shukla"),
  "S0056":_("Paramjit Gill"),
  "S0057":_("Ashok Kumar"),
  "S0058":_("P.M. Das"),
  "S0059":_("C. Pal Singh"),
  "S0060":_("Chander Shekhar"),
  "S0061":_("G.S. [Gurbachan Singh] Mann"),
  "S0062":_("R.S. [Rajdeep Singh] Gill"),
  "S0063":_("A.A. Siddique"),
  "S0064":_("Harbhajan Chand"),
  "S0065":_("Jagdish Kumar"),
  "S0066":_("Ishwar Chander Sharma"),
  "S0067":_("Iqbal Preet Singh Sahota"),
  "S0068":_("Anil Kaushik"),
  "S0069":_("Chaman Lal"),
  "S0070":_("Gurcharan Singh"),
  "S0071":_("Sukhdev Chhina"),
  "S0072":_("Bakhshi Ram"),
  "S0073":_("O.P. [Om Parkash] Sharma"),
  "S0074":_("R.S. Khatra"),
  "S0075":_("V.K. Bhawra"),
  "S0076":_("Rajan Gupta"),
  "S0077":_("Sarabjit Singh"),
  "S0078":_("Rohit Choudhary"),
  "S0079":_("V.N. Singh"),
  "S0080":_("S.K. Verma"),
  "S0081":_("J.F. Ribeiro"),
  "S0082":_("H.R. Chadha"),
  "S0083":_("Rajpal Meena"),
  "S0084":_("R.C. Singh"),
  "S0085":_("K.L. Likhi"),
  "S0086":_("Jagdish Mittal"),
  "S0087":_("S.S. [Sukhdyal Singh] Bhullar"),
  "S0088":_("Sube Singh"),
  "S0089":_("Daljit Singh Bhullar"),
  "S0090":_("R.P. Singh"),
  "S0091":_("Janngi Singh"),
  "S0092":_("Gian Singh"),
  "S0093":_("Gurbachan Jagat"),
  "S0094":_("Surjit Singh Bains"),
  "S0095":_("V.K. Rajagopalan"),
  "S0096":_("M.P. Singh"),
  "S0097":_("S. Bhullar"),
  "S0098":_("R.L. Wadhwa"),
  "S0099":_("S.S. Virk"),
  "S0100":_("Sudarshan Singh"),
  "S0101":_("Jarnail Singh Chahal"),
  "S0102":_("G.S. Aujla"),
  "S0103":_("Gurdial Singh"),
  "S0104":_("S.S. Nahar"),
  "S0105":_("S.R. Sharma"),
  "S0106":_("Devinder Singh"),
  "S0107":_("H.K.L. Dewan"),
  "S0108":_("S.C. Jain"),
  "S0109":_("Joginder Singh"),
  "S0110":_("A.K. Sarbhadhikari"),
  "S0111":_("R.P. Joshi"),
  "S0112":_("P.G. Harlankar"),
  "S0113":_("Parkash Singh"),
  "S0114":_("V.K. Sirdhi"),
  "S0115":_("Arvinder Singh Brar"),
  "S0116":_("Gurpreet Singh Dhillon"),
  "S0117":_("Balkar Singh"),
  "S0118":_("H.P. Bhatnagar"),
  "S0119":_("T. Anthachari"),
  "S0120":_("P.N. Ramakrishnan"),
  "S0121":_("K.R.K. Prasad"),
  "S0122":_("B.S. Bisht"),
  "S0123":_("Arjun Singh"),
  "S0124":_("S.M. Sharma"),
  "S0125":_("Ashok Patel"),
  "S0126":_("Beant Singh"),
  "S0127":_("R.K. Mehta"),
  "S0128":_("B.S. Tyagi"),
  "S0129":_("B.S. Sandhu"),
  "S0130":_("A.S. Atwal"),
  "S0131":_("G.S. Yadav"),
  "S0132":_("B.S. Suhag"),
  "S0133":_("Y.S. Bhatti"),
  "S0134":_("Udaibir Singh"),
  "S0135":_("Sunith Francis Rodrigues"),
  "S0136":_("V.K. Nayar"),
  "S0137":_("Parodh Kumar"),
  "S0138":_("Harinder Singh"),
  "S0139":_("N.S. Gill"),
  "S0140":_("B.P. Nawani"),
  "S0141":_("Gurdarshan Singh"),
  "S0142":_("A.K. Mittal"),
  "S0143":_("Ramesh  Chander"),
  "S0144":_("U.K. Bhavra"),
  "S0145":_("Shashi Kant"),
  "S0146":_("B.S. Gill"),
  "S0147":_("Sudharshan Likhi"),
  "S0148":_("J.P. Mohla"),
  "S0149":_("Swarn Singh"),
  "S0150":_("Ravinderpal Singh"),
  "S0151":_("S.N. Mathur"),
  "S0152":_("B.T. Pandit"),
  "S0153":_("A.C. Sharma"),
  "S0154":_("R.P. Singh"),
  "S0155":_("Barjinder Kumar"),
  "S0156":_("U.K. Chaudhury"),
  "S0157":_("A.S. Shaheed"),
  "S0158":_("Sita Ram Rattan"),
  "S0159":_("Sutanter Pal Singh (S.P.S.) Basra"),
}
#  "S0010":"Bua Singh",
#  "S0022":"Mahinder Singh",
#  "S0025":"Ravinderpal Singh",
#  "S0029":"Bakhshi Ram",


so_has_detail = ['S0001','S0002','S0009','S0024']


@register.filter(name='seniorofficial')
def seniorofficial(value):
    return officials.get(value)



@cache_page(60 * 60)
def perpetrators(request):
    
    s_officials = sorted(officials.items(), key=operator.itemgetter(1))    
    p_officials = []
    
    for o in s_officials:
      soas = SecurityArrest.objects.filter(soa_code=o[0]).count()
      soks = SecurityKilled.objects.filter(sok_code=o[0]).count()
      p = o + (soas + soks,)
      p_officials.append(p)

    return render(request, "perpetrators.html", { "officials": p_officials, "so_has_detail": so_has_detail })



@cache_page(60 * 60)
def robots(request):
    return render(request, "robots.txt")



@cache_page(60 * 60)
def official(request, slug=None):

    if slug in so_has_detail:
      if get_language() == 'pb':
        return redirect("/pb/official/"+slug+"/detail/")
      else:
        return redirect("/official/"+slug+"/detail/")

    name =  officials.get(slug)

    district = Villages.objects.filter(vid=OuterRef('village_id')).values('district')
    tehsil = Villages.objects.filter(vid=OuterRef('village_id')).values('tehsil')
    tehsil_id = Villages.objects.filter(vid=OuterRef('village_id')).values('tehsil_id')
    village = Villages.objects.filter(vid=OuterRef('village_id')).values('village_name')

    soas = SecurityArrest.objects.filter(soa_code=slug).values_list('record_id', flat=True)
    soks = SecurityKilled.objects.filter(sok_code=slug).values_list('record_id', flat=True)
    records = list(soas) + list(soks)
        
    victims = Data.objects.filter( record_id__in=records )\
      .annotate( village_name_checked=Subquery(village), district=Subquery(district), tehsil=Subquery(tehsil), tehsil_id=Subquery(tehsil_id) )\
      .order_by(F('district').asc(nulls_last=True),'tehsil','victim_name')

    stats = calculate_stats(victims)
    if id is not None and id is None:
        return messages.warning(request,"Official %s was not found"%id)
    return render(request, "securityforce.html", { "victims": victims, "name": name, "stats": stats, "slug": slug } )



@cache_page(60 * 60)
def official_detail(request, slug=None):

    district = Villages.objects.filter(vid=OuterRef('village_id')).values('district')
    tehsil = Villages.objects.filter(vid=OuterRef('village_id')).values('tehsil')
    tehsil_id = Villages.objects.filter(vid=OuterRef('village_id')).values('tehsil_id')
    village = Villages.objects.filter(vid=OuterRef('village_id')).values('village_name')

    soas = SecurityArrest.objects.filter(soa_code=slug).values_list('record_id', flat=True)
    soks = SecurityKilled.objects.filter(sok_code=slug).values_list('record_id', flat=True)
    records = list(soas) + list(soks)
        
    victims = Data.objects.filter( record_id__in=records )\
      .annotate( village_name_checked=Subquery(village), district=Subquery(district), tehsil=Subquery(tehsil), tehsil_id=Subquery(tehsil_id) )\
      .order_by(F('district').asc(nulls_last=True),'tehsil','victim_name')

    stats = calculate_stats(victims)

    if slug in so_has_detail:
      return render(request, "dossiers/official_detail_" + slug + ".html", {"stats": stats} )
    else:
      return messages.warning(request,"Official %s was not found"%id)



@cache_page(60 * 60)
def locality(request, slug=None):
    vid = slug

    _arrest_so_affiliation_loc = SecurityArrest.objects.filter(arrest_so_affiliation_loc__contains=vid).values_list('record_id', flat=True)
    _query = Q(arrest_security_locality__contains=vid) | Q(killing_securityforces_lcl__contains=vid) | Q( record_id__in= _arrest_so_affiliation_loc )

    name = get_village_name(vid)
    name_pb = get_village_name_pb(vid)

    district = Villages.objects.filter(vid=OuterRef('village_id')).values('district')
    tehsil = Villages.objects.filter(vid=OuterRef('village_id')).values('tehsil')
    tehsil_id = Villages.objects.filter(vid=OuterRef('village_id')).values('tehsil_id')
    village = Villages.objects.filter(vid=OuterRef('village_id')).values('village_name')

    victims = Data.objects.filter( _query )\
      .annotate( village_name_checked=Subquery(village), district=Subquery(district), tehsil=Subquery(tehsil), tehsil_id=Subquery(tehsil_id) )\
      .order_by(F('district').asc(nulls_last=True),'tehsil','victim_name')

    stats = calculate_stats(victims)
    if vid is not None and vid is None:
        return messages.warning(request,"Locality %s was not found"%vid)
    return render(request, "locality.html", { "victims": victims, "name": name, "name_pb": name_pb, "stats": stats } )



@cache_page(60 * 60)
def cremation(request, slug=None):
    vid = slug

    name = get_village_name(vid)
    name_pb = get_village_name_pb(vid)

    district = Villages.objects.filter(vid=OuterRef('village_id')).values('district')
    tehsil = Villages.objects.filter(vid=OuterRef('village_id')).values('tehsil')
    tehsil_id = Villages.objects.filter(vid=OuterRef('village_id')).values('tehsil_id')
    village = Villages.objects.filter(vid=OuterRef('village_id')).values('village_name')

    victims = Data.objects.filter( cremation_location_name__contains=vid )\
      .annotate( village_name_checked=Subquery(village), district=Subquery(district), tehsil=Subquery(tehsil), tehsil_id=Subquery(tehsil_id) )\
      .order_by(F('district').asc(nulls_last=True),'tehsil','victim_name')

    stats = calculate_stats(victims)
    if vid is not None and vid is None:
        return messages.warning(request,"Cremation Location %s was not found"%vid)
    return render(request, "cremation.html", { "victims": victims, "name": name, "name_pb": name_pb, "stats": stats } )




@cache_page(60 * 60)
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
    
    district = Villages.objects.filter(vid=OuterRef('village_id')).values('district')
    tehsil = Villages.objects.filter(vid=OuterRef('village_id')).values('tehsil')
    tehsil_id = Villages.objects.filter(vid=OuterRef('village_id')).values('tehsil_id')
    village = Villages.objects.filter(vid=OuterRef('village_id')).values('village_name')

    victims = Data.objects.filter( _query )\
      .annotate( village_name_checked=Subquery(village), district=Subquery(district), tehsil=Subquery(tehsil), tehsil_id=Subquery(tehsil_id) )\
      .order_by(F('district').asc(nulls_last=True),'tehsil','victim_name')

    stats = calculate_stats(victims)
    if slug is not None and slug is None:
        return messages.warning(request,"Security Force %s was not found"%slug)
    return render(request, "securityforce.html", { "victims": victims, "name": name, "stats": stats } )



@cache_page(60 * 60)
def tehsil(request, slug=None):
    datas = Data.objects.filter(village_id=OuterRef('pk'))\
                            .values('village_id')\
                            .annotate(Count('village_id'))\
                            .values('village_id__count')    

    villages_with_count = Villages.objects.filter(tehsil_id=slug)\
                                  .annotate(data_count=Subquery(datas))\
                                  .exclude(data_count=None).order_by('village_name')

    villages = Villages.objects.filter(tehsil_id=slug).values('vid','district','district_id','tehsil')

    all = Data.objects.filter(village_id__in=Subquery(villages.values('vid'))).order_by('victim_name')
    stats = calculate_stats(all)

    district_id = int(slug)

    return render(request, "tehsil.html", {
      'district_id': district_id,
      'villages_with_count': villages_with_count,
      'villages': villages,
      "stats": stats
      })



def get_first_names():
    first_names = cache.get("first_names")
    first_names_pb = cache.get("first_names_pb")

    if get_language() == 'pb':
      if first_names_pb:
          return first_names_pb
      try:
          first_names_pb = Data.objects.all()\
                          .values('victim_first_name_pb')\
                          .distinct().order_by('victim_first_name_pb')
          cache.set("first_names_pb", first_names_pb, 3600) # 60 * 60 seconds
          return first_names_pb
      except Exception as e:
          return messages.warning("Exception get_first_names:"%e)
          return None
    else:
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
     

def get_village_name(value):
    if value:
      try:
        village_name = Villages.objects.filter(vid=value).values('village_name')[:1].get()
        return village_name['village_name']
      except Exception as e:
        return None        
    else:
      return None

def get_village_name_pb(value):
    if value:
      try:
        village_name = Villages.objects.filter(vid=value).values('village_name_pb')[:1].get()
        return village_name['village_name_pb']
      except Exception as e:
        return None        
    else:
      return None

def get_tehsil_name(value):
    if value:
      tehsil_name = Villages.objects.filter(tehsil_id=value).values('tehsil')[:1].get()
      return tehsil_name['tehsil']
    else:
      return None

def get_district_name(value):
    if value:
      if len(value) < 4:
        district_name = Villages.objects.filter(district_id=value).values('district')[:1].get()
        return district_name['district']      
      else:
        district_name = Villages.objects.filter(tehsil_id=value).values('tehsil')[:1].get()
        return district_name['tehsil']      
    else:
      return None


def get_tehsils(slug):
    tehsils = cache.get("tehsils" + slug)
    if tehsils:
        return tehsils
    try:
      tehsils = Villages.objects.filter(district_id=slug)\
                        .values('tehsil', 'tehsil_id')\
                        .order_by('tehsil')\
                        .distinct()
      for tehsil in tehsils:
          datas = Data.objects.filter(village_id=OuterRef('pk'))\
                              .values('village_id')\
                              .annotate(Count('village_id'))\
                              .values('village_id__count')
          villages_data_count = Villages.objects.filter(tehsil_id=tehsil.get('tehsil_id'))\
                                        .values('vid')\
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



@cache_page(60 * 60)
def district(request, slug=None):
    tehsils = get_tehsils(slug)
    villages = Villages.objects.filter(district_id=slug).order_by('village_name')
    district = Villages.objects.filter(district_id=slug)[:1].values('district')
    all = Data.objects.filter(village_id__in=Subquery(villages.values('vid'))).order_by('victim_name')
    stats = calculate_stats(all)    
    district_id = int(slug)
    
    return render(request, "district.html", {
      "district_id": district_id,
      "district": district,
      "villages": tehsils,
      "stats": stats
      })


@cache_page(60 * 60)
def page(request, directory=None, slug=None):
    page = Page.objects.get(slug=slug)
    if slug is not None and page is None:
        return messages.warning(request,"page %s was not found"%slug)
    return render(request, "page.html", { "page":page } )






# email forms

def emailView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Case Update'
            from_email = form.cleaned_data['from_email']
            referer = form.cleaned_data['referer']

            message = "-------\n\nFrom: " + from_email + "\n\n-------\n\nVia: " + referer + "\n\n-------\n\n" + form.cleaned_data['message']

            msg = EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                ['john@backspace.com','jkaur@ensaaf.org','sdhami@ensaaf.org'],
                reply_to=[from_email],
            )
            msg.send()
            return render(request, "success.html", {"referer":referer})
    else:
      return render(request, "email.html")

def successView(request):
    return render(request, "success.html")





def vikusdata(request):
    victim_list = Data.objects.all().values(\
      'victim_name',
			'victim_disappeared_killed',
			'victim_death_date',
			'victim_arrest_date',
			'timeline_start',
			'timeline_end',
			'village_name',
			'photo_vic_fn',
			'record_id',
			'village_name',
			'victim_sex')\
      .annotate(year=Trunc('timeline', 'year', output_field=DateField() ))\
      .order_by('-timeline')
    return render(request, "vikus/data.html", { "victims":victim_list } )




@register.simple_tag()
def dossier_command(geo, slug, start, end):

  if geo == 'vid':
    all = Data.objects.filter( Q(timeline_start__gte=start), Q(timeline_end__lte=end), \
      village_id=slug, victim_arrest_location=2).order_by('record_id') \
      | Data.objects.filter(  Q(arrest_start__gte=start), Q(arrest_end__lte=end), \
      village_id=slug, victim_arrest_location=2).order_by('record_id')

    vids_for_mysql_regex = slug
    
  else:
    geo_id = geo + '_id'

    villages = Villages.objects.filter( **{geo_id: slug} ).values('vid','district','district_id','tehsil')

    all = Data.objects.filter( \
        Q(timeline_start__gte=start), Q(timeline_end__lte=end), \
        village_id__in=Subquery(villages.values('vid')), \
        victim_arrest_location=2).order_by('record_id'
      ) | \
      Data.objects.filter( \
        Q(arrest_start__gte=start), Q(arrest_end__lte=end), \
        village_id__in=Subquery(villages.values('vid')), \
        victim_arrest_location=2 \
      ).order_by('record_id')

    vids = Villages.objects.filter( **{geo_id: slug} ).values_list('vid', flat=True)
    seperator = '|'
    vids_for_mysql_regex = seperator.join(vids)


  if vids_for_mysql_regex:

    also = Data.objects.filter( \
        Q(timeline_start__gte=start), Q(timeline_end__lte=end), \
        Q(arrest_security_locality__iregex=vids_for_mysql_regex) | \
        Q(killing_securityforces_lcl__iregex=vids_for_mysql_regex) \
      ) | \
      Data.objects.filter(\
         Q(arrest_start__gte=start), Q(arrest_end__lte=end), \
         Q(arrest_security_locality__iregex=vids_for_mysql_regex) | \
         Q(killing_securityforces_lcl__iregex=vids_for_mysql_regex) ) 

    all = all | also

  # exclude non-police
  all = all.exclude( \
    Q(arrest_security_type_1 = 0, arrest_security_type_5=0, arrest_security_type_2=1) | \
    Q(arrest_security_type_1 = 0, arrest_security_type_5=0, arrest_security_type_3=1) | \
    Q(arrest_security_type_1 = 0, arrest_security_type_5=0, arrest_security_type_4=1) | \
    Q(killing_securityforcestype_1=0, killing_securityforcestype_5=0, killing_securityforcestype_2=1) | \
    Q(killing_securityforcestype_1=0, killing_securityforcestype_5=0, killing_securityforcestype_3=1) | \
    Q(killing_securityforcestype_1=0, killing_securityforcestype_5=0, killing_securityforcestype_4=1) \
    )

  return serializers.serialize("json", all, fields=('victim_name','victim_name_pb','village_id','village_name','village_name_pb','timeline','photo_vic_fn'))



@register.simple_tag()
def dossier_by_id(slug=None):
    ids =  slug.split(',')

    district = Villages.objects.filter(vid=OuterRef('village_id')).values('district')
    tehsil = Villages.objects.filter(vid=OuterRef('village_id')).values('tehsil')
    tehsil_id = Villages.objects.filter(vid=OuterRef('village_id')).values('tehsil_id')
    village = Villages.objects.filter(vid=OuterRef('village_id')).values('village_name')
        
    victims = Data.objects.filter( record_id__in=ids )\
      .annotate( village_name_checked=Subquery(village), district=Subquery(district), tehsil=Subquery(tehsil), tehsil_id=Subquery(tehsil_id) )\
      .order_by(F('district').asc(nulls_last=True),'tehsil','victim_name')

    return serializers.serialize("json", victims, fields=('victim_name','village_id','village_name','timeline'))



@register.simple_tag()
def dossier_abduction(slug=None):
    name =  officials.get(slug)

    district = Villages.objects.filter(vid=OuterRef('village_id')).values('district')
    tehsil = Villages.objects.filter(vid=OuterRef('village_id')).values('tehsil')
    tehsil_id = Villages.objects.filter(vid=OuterRef('village_id')).values('tehsil_id')
    village = Villages.objects.filter(vid=OuterRef('village_id')).values('village_name')

    soas = SecurityArrest.objects.filter(soa_code=slug).values_list('record_id', flat=True)
    soks = SecurityKilled.objects.filter(sok_code=slug).values_list('record_id', flat=True)
    records = list(soas) + list(soks)
        
    victims = Data.objects.filter( record_id__in=records )\
      .annotate( village_name_checked=Subquery(village), district=Subquery(district), tehsil=Subquery(tehsil), tehsil_id=Subquery(tehsil_id) )\
      .order_by(F('district').asc(nulls_last=True),'tehsil','victim_name','victim_name')

    return serializers.serialize("json", victims, fields=('victim_name','victim_name_pb','village_id','village_name','timeline'))





# from pprint import pprint

spellings = [ ['gurjit','gurjeet'] ]

def spelling(request):
    query = request.GET.get('q', '')
    manualmatch = ''
    for sublist in spellings:
        if sublist[1] == query:
            manualmatch = sublist[0]
            break
        elif sublist[0] == query:
            manualmatch = sublist[1]
            break
    results = vars( solr.search(query) )
    if manualmatch:
      try:
        results['spellcheck']['suggestions'][query]['suggestion'].insert(0, {'word': manualmatch,'freq': 25})
      except Exception: 
        results['spellcheck']['suggestions'][query] = {'suggestion': [ {'word': manualmatch,'freq': 25} ]}
        pass
    the_data = json.dumps({ 'results': results })
    return HttpResponse(the_data, content_type='application/json')

def autocomplete(request):
    sqs1 = SearchQuerySet().autocomplete(village_name=request.GET.get('q', ''))[:10]
    sqs2 = SearchQuerySet().autocomplete(victim_name=request.GET.get('q', ''))[:10]
    suggestions = [result.village_name for result in sqs1] + [result.victim_name for result in sqs2]
    the_data = json.dumps({ 'results': suggestions })
    return HttpResponse(the_data, content_type='application/json')
