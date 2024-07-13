from django.urls import path
from blog_api.views import PostListCreate, PostDetail
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", PostListCreate.as_view(), name="post_list"),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('posts/', BlogPostListCreate.as_view(), name='post-list-create'),
    # path('posts/<int:pk>/', BlogPostDetail.as_view(), name='post-detail'),
]
