from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl import DocType, Index
from .models import Data, Villages



data = Index('data')
data.settings( number_of_shards=1, number_of_replicas=0 )

@data.doc_type
class DataDocument(DocType):
    class Meta:
        model = Data
        fields = [
            'record_id',
            'victim_name',
            'village_name',
            'photo_vic_fn',
            'photo_vic_fn',
            'victim_disappeared_killed',
            'timeline_start',
            'timeline_end',
        ]



villages = Index('villages')
villages.settings( number_of_shards=1, number_of_replicas=0 )

@villages.doc_type
class VillagesDocument(DocType):
    class Meta:
        model = Villages
        fields = [
            'id',
            'village_name',
            'tehsil',
            'district',
            'tehsil_id',
            'district_id',
            'lat',
            'lon',
        ]
        