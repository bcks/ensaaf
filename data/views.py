from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache import cache
from django.contrib import messages
from django.db.models import OuterRef, Subquery, Count, Sum
from django.template.defaulttags import register

from .models import *
from django.shortcuts import render



def home(request):    
    all = Data.objects.all();
    victims = all.order_by('?')[:20]
    total_disappeared = all.filter(victim_disappeared_killed='1').count()
    total_killed = all.filter(victim_disappeared_killed='2').count()
    male = all.filter(victim_sex='1').count()
    female = all.filter(victim_sex='2').count()
    married = all.filter(victim_marital_status='1').count()
    not_married = all.filter(victim_marital_status='0').count()
    genuine_encounter = all.filter(genuine_encounters='1').count()
    not_genuine_encounter = all.filter(genuine_encounters='0').count()
    kesdhari = all.filter(victim_kesdhari='1').count()
    amritdhari = all.filter(victim_amritdhari='1').count()
    militant = all.filter(victim_militant_status='1').count()
    not_militant = all.filter(victim_militant_status='0').count()
    militant_support = all.filter(victim_militant_support='1').count()
    no_militant_support = all.filter(victim_militant_support='0').count()
    prior_detentions = all.filter(victim_prior_detention_st='1').count()
    no_prior_detentions = all.filter(victim_prior_detention_st='0').count()
    security_officials_apprchd = all.filter(security_officials_apprchd='1').count()
    no_security_officials_apprchd = all.filter(security_officials_apprchd='0').count()
    court_or_commission = all.filter(court_or_commission='1').count()
    no_court_or_commission = all.filter(court_or_commission='0').count()
    return render(request, "home.html", { 
      "victims": victims,
      "total_disappeared": total_disappeared,
      "total_killed": total_killed,
      "male": male,
      "female": female,
      "married": married,
      "not_married": not_married,
      "genuine_encounter": genuine_encounter,
      "not_genuine_encounter": not_genuine_encounter,
      "kesdhari": kesdhari,
      "amritdhari": amritdhari,
      "militant": militant,
      "not_militant": not_militant,
      "militant_support": militant_support,
      "no_militant_support": no_militant_support,
      "prior_detentions": prior_detentions,
      "no_prior_detentions": no_prior_detentions,
      "security_officials_apprchd": security_officials_apprchd,
      "no_security_officials_apprchd": no_security_officials_apprchd,
      "court_or_commission": court_or_commission,
      "no_court_or_commission": no_court_or_commission,
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
    total_disappeared = all.filter(victim_disappeared_killed='1').count()
    total_killed = all.filter(victim_disappeared_killed='2').count()
    male = all.filter(victim_sex='1').count()
    female = all.filter(victim_sex='2').count()
    married = all.filter(victim_marital_status='1').count()
    not_married = all.filter(victim_marital_status='0').count()
    genuine_encounter = all.filter(genuine_encounters='1').count()
    not_genuine_encounter = all.filter(genuine_encounters='0').count()
    kesdhari = all.filter(victim_kesdhari='1').count()
    amritdhari = all.filter(victim_amritdhari='1').count()
    militant = all.filter(victim_militant_status='1').count()
    not_militant = all.filter(victim_militant_status='0').count()
    militant_support = all.filter(victim_militant_support='1').count()
    no_militant_support = all.filter(victim_militant_support='0').count()
    prior_detentions = all.filter(victim_prior_detention_st='1').count()
    no_prior_detentions = all.filter(victim_prior_detention_st='0').count()
    security_officials_apprchd = all.filter(security_officials_apprchd='1').count()
    no_security_officials_apprchd = all.filter(security_officials_apprchd='0').count()
    court_or_commission = all.filter(court_or_commission='1').count()
    no_court_or_commission = all.filter(court_or_commission='0').count()

    return render(request, "tehsil.html", {
      "villages": villages,
      "total_disappeared": total_disappeared,
      "total_killed": total_killed,
      "male": male,
      "female": female,
      "married": married,
      "not_married": not_married,
      "genuine_encounter": genuine_encounter,
      "not_genuine_encounter": not_genuine_encounter,
      "kesdhari": kesdhari,
      "amritdhari": amritdhari,
      "militant": militant,
      "not_militant": not_militant,
      "militant_support": militant_support,
      "no_militant_support": no_militant_support,
      "prior_detentions": prior_detentions,
      "no_prior_detentions": no_prior_detentions,
      "security_officials_apprchd": security_officials_apprchd,
      "no_security_officials_apprchd": no_security_officials_apprchd,
      "court_or_commission": court_or_commission,
      "no_court_or_commission": no_court_or_commission,
      })


def district(request, slug=None):
    villages = Villages.objects.filter(district_id=slug).order_by('village_name')

    all = Data.objects.filter(village_id__in=Subquery(villages.values('id'))).order_by('victim_name')
    total_disappeared = all.filter(victim_disappeared_killed='1').count()
    total_killed = all.filter(victim_disappeared_killed='2').count()
    male = all.filter(victim_sex='1').count()
    female = all.filter(victim_sex='2').count()
    married = all.filter(victim_marital_status='1').count()
    not_married = all.filter(victim_marital_status='0').count()
    genuine_encounter = all.filter(genuine_encounters='1').count()
    not_genuine_encounter = all.filter(genuine_encounters='0').count()
    kesdhari = all.filter(victim_kesdhari='1').count()
    amritdhari = all.filter(victim_amritdhari='1').count()
    militant = all.filter(victim_militant_status='1').count()
    not_militant = all.filter(victim_militant_status='0').count()
    militant_support = all.filter(victim_militant_support='1').count()
    no_militant_support = all.filter(victim_militant_support='0').count()
    prior_detentions = all.filter(victim_prior_detention_st='1').count()
    no_prior_detentions = all.filter(victim_prior_detention_st='0').count()
    security_officials_apprchd = all.filter(security_officials_apprchd='1').count()
    no_security_officials_apprchd = all.filter(security_officials_apprchd='0').count()
    court_or_commission = all.filter(court_or_commission='1').count()
    no_court_or_commission = all.filter(court_or_commission='0').count()
    
    villages_distinct = Villages.objects.filter(district_id=slug).values('district','tehsil','tehsil_id').distinct()
    
    return render(request, "district.html", {
      "villages": villages_distinct,
      "total_disappeared": total_disappeared,
      "total_killed": total_killed,
      "male": male,
      "female": female,
      "married": married,
      "not_married": not_married,
      "genuine_encounter": genuine_encounter,
      "not_genuine_encounter": not_genuine_encounter,
      "kesdhari": kesdhari,
      "amritdhari": amritdhari,
      "militant": militant,
      "not_militant": not_militant,
      "militant_support": militant_support,
      "no_militant_support": no_militant_support,
      "prior_detentions": prior_detentions,
      "no_prior_detentions": no_prior_detentions,
      "security_officials_apprchd": security_officials_apprchd,
      "no_security_officials_apprchd": no_security_officials_apprchd,
      "court_or_commission": court_or_commission,
      "no_court_or_commission": no_court_or_commission,
      })


