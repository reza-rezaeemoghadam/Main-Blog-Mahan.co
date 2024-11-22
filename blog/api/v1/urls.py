# Importing restframework modules
from rest_framework.urls import path

# Import views
from blog.api.v1.views import CommentCreateAPIView

app_name = 'user'

urlpatterns = [
    path("post/comment/", CommentCreateAPIView.as_view(), name="comment-insert"),
]