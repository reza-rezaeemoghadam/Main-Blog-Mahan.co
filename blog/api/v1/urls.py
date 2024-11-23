# Importing restframework modules
from rest_framework.urls import path

# Import views
from blog.api.v1.views import CommentCreateAPIView, PostDetailView, PostMainPageView, PostListAPIView

app_name = 'user'

urlpatterns = [
    path("post/comment/", CommentCreateAPIView.as_view(), name="comment-insert"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/", PostListAPIView.as_view(), name="post-list"),
    path("post/main-page/", PostMainPageView.as_view(), name="post-main-page"),
]