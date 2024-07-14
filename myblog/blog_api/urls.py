from django.urls import path
from blog_api.views import PostListCreate, PostDetail


urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", PostListCreate.as_view(), name="post_list"),
]
