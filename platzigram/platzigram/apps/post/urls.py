from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import create_post, PostsFeedView, PostDetailView

urlpatterns = [
    path('', PostsFeedView.as_view(), name='feed'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('posts/new/', login_required(create_post), name='create_post'),
]