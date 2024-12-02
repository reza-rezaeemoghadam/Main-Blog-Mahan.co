# Improting rest framework modules
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

# Importing custom models
from website.models import Section, Part, ContactUs, VisitUs, SocialLinks


# Implementing base serializers
class BaseVisitUsSerializer(ModelSerializer):
    class Meta:
        model = VisitUs
        fields = ['address', 'phone', 'email']

class BaseSocialLinksSerializer(ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = ['name', 'icon', 'url']
        
class BasePartSerializer(ModelSerializer):
    class Meta:
        model = Part
        fields = ['id','title','sub_title', 'content','image', 'url', 'number']

class BaseSectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'title', 'content', 'number']
# Implementing serializers
class FullPortionContactUsSerializer(ModelSerializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    website = serializers.URLField(required=True)
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'phone', 'content', 'website']

class FullPortionVisitUsSerializer(ModelSerializer):
    class Meta:
        model = VisitUs
        fields = '__all__'

class FullPortionSocialLinksSerializer(ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = '__all__'
        
class FullPortionPartSerialzer(BasePartSerializer):
    class Meta(BasePartSerializer.Meta):
        fields = BasePartSerializer.Meta.fields + ['section']

class FullPortionSectionSerializers(BaseSectionSerializer):
    parts = FullPortionPartSerialzer(many=True, read_only=True)
    visit_us = BaseVisitUsSerializer(many=False, read_only=True)
    social_links = BaseSocialLinksSerializer(many=True, read_only=False)
    class Meta(BaseSectionSerializer.Meta):
        fields = BaseSectionSerializer.Meta.fields + ['parts', 'social_links', 'visit_us']