# Import restframework module
from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField

# Import models
from blog.models import Post, Comment

# Create serializers
class MediaSerializer(serializers.ModelSerializer):
    pass
    class Meta:
        pass

class PostSerializer(serializers.ModelSerializer):
    pass
    class Meta:
        model = Post
        field = []

class CommentSerializer(serializers.ModelSerializer):
    post = PrimaryKeyRelatedField(queryset=Post.objects.all(), required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone  = serializers.CharField(required=True)

    class Meta:
        model = Comment
        fields = ["post", "first_name", "last_name", "phone", "content"]