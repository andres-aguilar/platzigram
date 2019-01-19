from django.urls import path

from .views import PostsFeedView, PostDetailView, CreatePostView

urlpatterns = [
    path('', PostsFeedView.as_view(), name='feed'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('posts/new/', CreatePostView.as_view(), name='create_post'),
]