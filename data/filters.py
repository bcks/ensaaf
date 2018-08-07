from .models import Data
import django_filters


class DataFilter(django_filters.FilterSet):

  age = django_filters.CharFilter(method='age_filter')
  def age_filter(self, queryset, name, value):
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

  gender = django_filters.CharFilter(method='gender_filter')
  def gender_filter(self, queryset, name, value):
    if value == 'Male':
      return queryset.filter(**{'victim_sex': '1'})    
    elif value == 'Female':
      return queryset.filter(**{'victim_sex': '2'})

  religion = django_filters.CharFilter(method='religion_filter')
  def religion_filter(self, queryset, name, value):
    indexNumber = ['X','Sikh','Hinduism','Islam','Christianity','No religion','Don’t know','Other'].index(value)
    if indexNumber:
      return queryset.filter(**{'victim_religion': indexNumber})    
    
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
      'age',
      'caste',
      'classification',
      'gender',
      'religion',
      'year',
    ]
