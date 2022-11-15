import graphene
from graphene_django import DjangoObjectType
from .models import NYCBuilding
from .views import get_nyc_api_data


class NYCBuildingType(DjangoObjectType):
    class Meta:
        model = NYCBuilding
        fields = ('id', 'address', 'zip_code', 'state', 'yrbuild', 'pytaxclass', 'owner', 'gross_sqft', 'building_city')


class Query(graphene.ObjectType):
    buildings = graphene.List(NYCBuildingType)
    building = graphene.Field(NYCBuildingType, id=graphene.Int(), address=graphene.String(), zip_code=graphene.String())
    @staticmethod
    def resolve_buildings(root, info):
        return NYCBuilding.objects.all()

    @staticmethod
    def resolve_building(self, info, **kwargs):
        id = kwargs.get('id')
        address = kwargs.get('address', None)
        zip_code = kwargs.get('zip_code', None)
        if not address:
            return NYCBuilding.objects.get(id=id)
        if address and zip_code:
            return NYCBuilding.objects.get(zip_code=zip_code, address=address)
        return NYCBuilding.objects.get(id=id, address=address)


class CreateCategory(graphene.Mutation):
    status = graphene.String()
    error = graphene.String()

    @classmethod
    def mutate(cls, root, info):
        try:
            data = get_nyc_api_data()
            for building_info in data:
                building = NYCBuilding()
                building.address = building_info["address"]
                building.zip_code = building_info["zip_code"]
                building.gross_sqft = building_info["gross_sqft"]
                building.yrbuilt = building_info["yrbuilt"]
                building.pytaxclass = building_info["pytaxclass"]
                building.owner = building_info["owner"]
                building.save()
            return CreateCategory(status="success", error="false")
        except Exception as e:
            return CreateCategory(status="Faild", error=e)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)


















































































schema = graphene.Schema(query=Query, mutation=Mutation)
