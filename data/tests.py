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

    def test_district_village_annotation(self):
        """
        Test data:
        A District has 2 Subdistricts: T1 and T2.
        T1 has 2 villages: V1 and V2.
            V1 has 2 Data objects: D1 and D2.
            V2 has 1 Data object: D3
        T2 has 2 villages: V3 and V4.
        Neither V3 or V4 had any Data objects.
        """
        fields = Data._meta.get_fields()
        default_args = {}
        for field in fields:
            if isinstance(field, IntegerField):
                default_args[field.name] = 0
        village1 = Villages.objects.create(
            id=99,
            village_name='village1', 
            district_id=6,
            district='D1',
            tehsil='T1',
            tehsil_id=9)
        village2 = Villages.objects.create(
            id=98,
            village_name='village2', 
            district_id=6, 
            district='D1',
            tehsil='T1',            
            tehsil_id=9)
        village3 = Villages.objects.create(
            id=97,
            village_name='village2', 
            district_id=6, 
            district='D1',
            tehsil='T2',
            tehsil_id=10)                
        village4 = Villages.objects.create(
            id=96,
            village_name='village2', 
            district_id=6, 
            district='D1',
            tehsil='T2',
            tehsil_id=10)
        data1 = Data.objects.create(
            village_id=str(village1.id),
            **default_args
           )
        default_args['record_id'] = 1
        data2 = Data.objects.create(
            village_id=str(village1.id),
            **default_args
           )
        default_args['record_id'] = 2
        data3 = Data.objects.create(
            village_id=str(village2.id),
            **default_args
           )        
        slug = 6
        tehsils = Villages.objects.filter(district_id=slug)\
                                        .values('tehsil', 'tehsil_id')\
                                        .distinct()
        for tehsil in tehsils:
            datas = Data.objects.filter(village_id=OuterRef('pk'))\
                                .values('village_id')\
                                .annotate(Count('village_id'))\
                                .values('village_id__count')
            villages_data_count = Villages.objects.filter(tehsil_id=tehsil.get('tehsil_id'))\
                                            .values('id')\
                                            .annotate(data_count=Subquery(datas))\
                                            .order_by('-data_count')\
                                            .values('data_count')
            tehsil['data_count'] = villages_data_count.aggregate(Sum('data_count'))\
                                                        .get('data_count__sum')
        self.assertEqual(Villages.objects.count(), 4)
        self.assertEqual(Data.objects.count(), 3)  
        self.assertEqual(len(tehsils), 2)
        self.assertEqual(tehsils[0]['data_count'], None)
        self.assertEqual(tehsils[1]['data_count'], 3)