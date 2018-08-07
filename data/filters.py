from .models import Data
import django_filters


class DataFilter(django_filters.FilterSet):

  gender = django_filters.CharFilter(method='gender_filter')
  def gender_filter(self, queryset, name, value):
    if value == 'Male':
      return queryset.filter(**{'victim_sex': '1'})    
    elif value == 'Female':
      return queryset.filter(**{'victim_sex': '2'})
    
  year = django_filters.CharFilter(method='year_filter')
  def year_filter(self, queryset, name, value):
    if value == 'Date Unknown':
      return queryset.filter(**{'timeline__lte': '1979-12-31'})    
    else:
      startvalue = value + '-01-01'
      endvalue = value + '-12-31'
      return queryset.filter(**{
        'timeline_start__gte': startvalue,
        'timeline_end__lte': endvalue,
      })

  class Meta:
    model = Data
    fields = [
      'gender',
      'year',
    ]
