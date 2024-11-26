# Import restframework module
from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField

# Import models
from blog.models import Post, Comment, Media, Category


# Create base serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['media_type','description','file']

class BasePostSerializer(serializers.ModelSerializer):
    media = MediaSerializer(many=False, read_only=True)
    category = CategorySerializer(many=False, read_only=True)
    
    class Meta:
        model = Post
        fields = ['id','title', 'media']

# Create serializers
class FullPostSerializer(BasePostSerializer):
    class Meta(BasePostSerializer.Meta):
        fields = BasePostSerializer.Meta.fields + ['body', 'published_at', 'author']

class SummaryPostSerializer(BasePostSerializer):
    class Meta(BasePostSerializer.Meta):
        fields = BasePostSerializer.Meta.fields + ['id','abstract']

class CommentSerializer(serializers.ModelSerializer):
    post = PrimaryKeyRelatedField(queryset=Post.objects.all(), required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone  = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    class Meta:
        model = Comment
        fields = ["post", "first_name", "last_name", "phone", "content"]