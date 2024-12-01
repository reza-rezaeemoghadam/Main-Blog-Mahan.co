# Improting rest framework modules
from rest_framework.serializers import ModelSerializer

# Importing custom models
from website.models import Section, Part


# Implementing base serializers
class BasePartSerializer(ModelSerializer):
    class Meta:
        model = Part
        fields = ['id','title','sub_title', 'image', 'url', 'number']

class BaseSectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'title', 'content', 'number']
# Implementing serializers
class FullPortionPartSerialzer(BasePartSerializer):
    class Meta(BasePartSerializer.Meta):
        fields = BasePartSerializer.Meta.fields + ['section']

class FullPortionSectionSerializers(BaseSectionSerializer):
    parts = FullPortionPartSerialzer(many=True, read_only=True)
    class Meta(BaseSectionSerializer.Meta):
        fields = BaseSectionSerializer.Meta.fields + ['parts']