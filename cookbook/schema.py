import graphene
from graphene_django import DjangoObjectType

from cookbook.malzemeler.models import Category, Malzemeler

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")

class MazlzemelerType(DjangoObjectType):
    class Meta:
        model = Malzemeler
        fields = ("id", "name", "notes", "category")

class Query(graphene.ObjectType):
    all_ingredients = graphene.List(MazlzemelerType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_malzemelers(root, info):
        # We can easily optimize query count in the resolve method
        return Malzemeler.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)