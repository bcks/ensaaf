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
