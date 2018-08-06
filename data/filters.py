from .models import Lawsuits, Officers
import django_filters


class DataFilter(django_filters.FilterSet):
    
  year = django_filters.CharFilter(method='year_filter')
  def year_filter(self, queryset, name, value):
    return queryset.filter(**{
      'timline__gte': value,
      'timline__lte': value,
    })

  class Meta:
    model = Lawsuits
    fields = [
      'year',
#      'district__value',
#      'subdistrict__value',
#      'urbanrural__value',
#      'firstname__value',
#      'militant__value',
#      'gender__value',
#      'age__value',
#      'religion__value',
#      'classification',
    ]

  @property
  def qs(self):
      parent = super(LawsuitFilter, self).qs
      return parent.filter(year__gte=2015, federal=1)

