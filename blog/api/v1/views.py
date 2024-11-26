# Import django module
from django.utils import translation

# Import restframework module
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated 

# Import serializer
from blog.api.v1.serializers import (FullPostSerializer, SummaryPostSerializer, 
                                    CommentSerializer,) 

# Import models
from blog.models import Post, Comment

# Create views
class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all().exclude(is_draft=True)
    serializer_class = FullPostSerializer

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all().exclude(is_draft=True)
    serializer_class = FullPostSerializer

class PostMainPageView(ListAPIView):
    serializer_class = SummaryPostSerializer
    model = Post
    def get_queryset(self):
        top_n = self.request.query_params.get('top', None)
        current_language = translation.get_language()
        queryset = self.model.objects.language(current_language).all().order_by("-published_at").exclude(is_draft=True)
        if top_n and (len(queryset)<=int(top_n)):
            return queryset[:int(top_n)] 
        else:
            return queryset

    