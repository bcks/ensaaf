from django.test import TestCase
from django.db.models.fields import IntegerField
from .models import Data, Villages
from django.db.models import Count
from django.db.models import OuterRef, Subquery


class ViewTest(TestCase):


    def setUp(self):
        fields = Data._meta.get_fields()
        default_args = {}
        for field in fields:
            if isinstance(field, IntegerField):
                default_args[field.name] = 0
        village1 = Villages.objects.create(
            id=99,
            village_name='village1', 
            district_id=6, 
            tehsil_id=9)
        village2 = Villages.objects.create(
            id=98,
            village_name='village2', 
            district_id=7, 
            tehsil_id=8)        
        data1 = Data.objects.create(
            village_id=str(village1.id),
            **default_args
           )
        default_args['record_id'] = 1
        data2 = Data.objects.create(
            village_id=str(village1.id),
            **default_args
           )        
        self.assertEqual(Villages.objects.count(), 2)
        self.assertEqual(Data.objects.count(), 2)        

    def test_villages_annotation(self):

        # Create a subquery that returns only 1 column
        # and references the PK from the parent query.
        # The first .values() is present because calling .annotate() after
        # it acts like "GROUP BY", which returns a single row.
        # 
        # 'village_id__count' is the default annotation name.
        datas = Data.objects.filter(village_id=OuterRef('pk'))\
                                .values('village_id')\
                                .annotate(Count('village_id'))\
                                .values('village_id__count')
        # Annotate a new property on each <Villages> object 
        # a Subquery from above and order by this new property
        villages = Villages.objects.annotate(data_count=Subquery(datas))\
                                        .order_by('data_count')
        self.assertEqual(villages.count(), 2)
        self.assertEqual(villages[0].data_count, None)
        self.assertEqual(villages[1].data_count, 2)