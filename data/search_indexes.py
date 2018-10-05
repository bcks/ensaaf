import datetime
from haystack import indexes
from .models import *

class DataIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    record_id = indexes.IntegerField(model_attr='record_id', null=True)
    victim_name = indexes.CharField(model_attr='victim_name', null=True)
    village_name = indexes.CharField(model_attr='village_name', null=True)
    photo_vic_fn = indexes.CharField(model_attr='photo_vic_fn', null=True)
    victim_disappeared_killed = indexes.IntegerField(model_attr='victim_disappeared_killed', null=True)
    timeline_start = indexes.CharField(model_attr='timeline_start', null=True)
    timeline_end = indexes.CharField(model_attr='timeline_end', null=True)

    def get_model(self):
        return Data

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class VillageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    village_name = indexes.EdgeNgramField(model_attr='village_name', null=True)
    id = indexes.CharField(model_attr='id', null=True)
    tehsil = indexes.CharField(model_attr='tehsil', null=True)
    district = indexes.CharField(model_attr='district', null=True)
    district_id = indexes.IntegerField(model_attr='district_id', null=True)
    tehsil_id = indexes.IntegerField(model_attr='tehsil_id', null=True)
    lon = indexes.DecimalField(model_attr='lon', null=True)
    lat = indexes.DecimalField(model_attr='lat', null=True)

    def get_model(self):
        return Villages

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

    def prepare(self, obj):
        data = super(VillageIndex, self).prepare(obj)
        data['_boost'] = 3
        return data
