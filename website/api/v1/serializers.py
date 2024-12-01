# Improting rest framework modules
from rest_framework.serializers import ModelSerializer

# Importing custom models
from website.models import Section, Part


# Implementing base serializers
class BasePartSerializer(ModelSerializer):
    class Meta:
        model = Part
        field = ['id','title','sub_title', 'image', 'url', 'number']

class BaseSectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        field = ['id', 'title', 'content', 'number']
# Implementing serializers
class FullPortionPartSerialzer(BasePartSerializer):
    class Meta:
        field = BasePartSerializer.Meta.field + ['section']

class FullPortionSectionSerializers(ModelSerializer):
    parts = FullPortionPartSerialzer(many=True, readonly=True)
    class Meta:
        field = BaseSectionSerializer.Meta.field + ['parts']