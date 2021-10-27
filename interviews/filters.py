from .models import Video, Villages
import django_filters


class InterviewFilter(django_filters.FilterSet):

  age = django_filters.CharFilter(method='age_filter')
  def age_filter(self, queryset, name, value):
    if value == "65+":
      value = "65-99"
    age_start, age_end = value.split('-')
    return queryset.filter(**{
      'age__gte': age_start,
      'age__lte': age_end,
    })

  classification = django_filters.CharFilter(method='classification_filter')
  def classification_filter(self, queryset, name, value):
    if value == 'Enforced Disappearance':
      return queryset.filter(**{'classification': '1'})    
    elif value == 'Extrajudicial Execution':
      return queryset.filter(**{'classification': '2'})

  gender = django_filters.CharFilter(method='gender_filter')
  def gender_filter(self, queryset, name, value):
    if value == 'Male':
      return queryset.filter(**{'gender': '1'})    
    elif value == 'Female':
      return queryset.filter(**{'gender': '2'})

  district = django_filters.CharFilter(method='district_filter')
  def district_filter(self, queryset, name, value):
    if len(value) < 4:
      villages = Villages.objects.filter(district_id=value).order_by('village_name')
    else:
      villages = Villages.objects.filter(tehsil_id=value).order_by('village_name')
    return queryset.filter(**{'village__in': villages.values('vid') })

  combatant = django_filters.CharFilter(method='combatant_filter')
  def combatant_filter(self, queryset, name, value):
    if value == 'Combatant':
      return queryset.filter(**{'combatant_status': '1'})    
    elif value == 'Non-Combatant':
      return queryset.filter(**{'combatant_status': '0'})
    elif value == 'Unknown':
      return queryset.filter(**{'combatant_status': '9'})

  year = django_filters.CharFilter(method='year_filter')
  def year_filter(self, queryset, name, value):
    if value == 'Date Unknown':
      return queryset.filter(**{'year': None})
    if value == "ਪਤਾ ਨਹੀਂ":
      return queryset.filter(**{'year': None})
    else:
      startvalue = value + '-01-01'
      endvalue = value + '-12-31'
      return queryset.filter(**{
        'date_range_start__gte': startvalue,
        'date_range_end__lte': endvalue,
      })

  class Meta:
    model = Video
    fields = [
      'age',
      'classification',
      'district',
      'gender',
      'combatant',
      'year',
    ]