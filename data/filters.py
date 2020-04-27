from .models import Data, Villages, SecurityArrest, SecurityKilled
import django_filters


class DataFilter(django_filters.FilterSet):

  age = django_filters.CharFilter(method='age_filter')
  def age_filter(self, queryset, name, value):
    if value == "65+":
      value = "65-99"
    age_start, age_end = value.split('-')
    return queryset.filter(**{
      'victim_age__gte': age_start,
      'victim_age__lte': age_end,
    })

  caste = django_filters.CharFilter(method='caste_filter')
  def caste_filter(self, queryset, name, value):
    indexNumber = ['X', 'Jat','Ramgarhia','Dalit/SC/BC','Mazbi','Chamar','Khatri','Naee','Don’t know','Other'].index(value)
    if indexNumber:
      return queryset.filter(**{'victim_caste': indexNumber})    

  classification = django_filters.CharFilter(method='classification_filter')
  def classification_filter(self, queryset, name, value):
    if value == 'Enforced Disappearance':
      return queryset.filter(**{'victim_disappeared_killed': '1'})    
    elif value == 'Extrajudicial Execution':
      return queryset.filter(**{'victim_disappeared_killed': '2'})

  first_name = django_filters.CharFilter(method='first_name_filter')
  def first_name_filter(self, queryset, name, value):
    return queryset.filter(**{'victim_first_name': value})    

  urban_rural = django_filters.CharFilter(method='urban_rural_filter')
  def urban_rural_filter(self, queryset, name, value):
    if value == 'Urban':
      return queryset.filter(**{'urban_rural': '1'})    
    elif value == 'Rural':
      return queryset.filter(**{'urban_rural': '0'})

  gender = django_filters.CharFilter(method='gender_filter')
  def gender_filter(self, queryset, name, value):
    if value == 'Male':
      return queryset.filter(**{'victim_sex': '1'})    
    elif value == 'Female':
      return queryset.filter(**{'victim_sex': '2'})

  religion = django_filters.CharFilter(method='religion_filter')
  def religion_filter(self, queryset, name, value):
    indexNumber = ['X','Sikh','Hindu','Muslim','Christian','No religion','Don’t know','Other'].index(value)
    if indexNumber:
      return queryset.filter(**{'victim_religion': indexNumber})    

  district = django_filters.CharFilter(method='district_filter')
  def district_filter(self, queryset, name, value):
    if len(value) < 4:
      villages = Villages.objects.filter(district_id=value).order_by('village_name')
    else:
      villages = Villages.objects.filter(tehsil_id=value).order_by('village_name')
    return queryset.filter(**{'village_id__in': villages.values('vid') })

  combatant = django_filters.CharFilter(method='combatant_filter')
  def combatant_filter(self, queryset, name, value):
    if value == 'Combatant':
      return queryset.filter(**{'victim_militant_status': '1'})    
    elif value == 'Non-Combatant':
      return queryset.filter(**{'victim_militant_status': '0'})
    elif value == 'Unknown':
      return queryset.filter(**{'victim_militant_status': '9'})

  year = django_filters.CharFilter(method='year_filter')
  def year_filter(self, queryset, name, value):
    if value == 'Date Unknown':
      return queryset.filter(**{'timeline': None})
    if value == "ਪਤਾ ਨਹੀਂ":
      return queryset.filter(**{'timeline': None})
    else:
      startvalue = value + '-01-01'
      endvalue = value + '-12-31'
      return queryset.filter(**{
        'timeline__gte': startvalue,
        'timeline__lte': endvalue,
      })

  so = django_filters.CharFilter(method='so_filter')
  def so_filter(self, queryset, name, value):
    soas = SecurityArrest.objects.filter(soa_code=value).values_list('record_id', flat=True)
    soks = SecurityKilled.objects.filter(sok_code=value).values_list('record_id', flat=True)
    records = list(soas) + list(soks)
    return queryset.filter(**{'record_id__in': records })

  class Meta:
    model = Data
    fields = [
      'age',
      'caste',
      'classification',
      'district',
      'first_name',
      'gender',
      'urban_rural',
      'combatant',
      'religion',
      'year',
      'so',
    ]