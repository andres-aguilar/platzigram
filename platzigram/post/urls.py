from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import create_post, PostsFeedView

urlpatterns = [
    path('', PostsFeedView.as_view(), name='feed'),
    path('posts/new/', login_required(create_post), name='create_post'),
]