import datetime
from haystack import indexes
from .models import *

class DataIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    record_id = indexes.CharField(model_attr='record_id', null=True)
    victim_name = indexes.CharField(model_attr='victim_name', null=True)
    village_name = indexes.CharField(model_attr='village_name', null=True)

    def get_model(self):
        return Data

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class VillageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    village_name = indexes.CharField(model_attr='village_name', null=True)
    id = indexes.CharField(model_attr='id', null=True)
    tehsil = indexes.CharField(model_attr='tehsil', null=True)
    district = indexes.CharField(model_attr='district', null=True)
    district_id = indexes.CharField(model_attr='id', null=True)
    tehsil_id = indexes.CharField(model_attr='tehsil_id', null=True)

    def get_model(self):
        return Villages

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

    def prepare(self, obj):
        data = super(VillageIndex, self).prepare(obj)
        data['_boost'] = 3
        return data
