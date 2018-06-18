from .models import Data as DataModel
import graphene
from graphene import Schema, relay, resolve_only_args
from graphene_django import DjangoConnectionField, DjangoObjectType


class Data(DjangoObjectType):
    class Meta:
        model = DataModel

class Query(graphene.ObjectType):
    data = graphene.List(Data)

    def resolve_data(self, info):
        return DataModel.objects.filter(timeline__range=["1970-01-01", "1997-01-01"])


schema = graphene.Schema(query=Query)
