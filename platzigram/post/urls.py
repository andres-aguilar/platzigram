from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import list_posts, create_post

urlpatterns = [
    path('', login_required(list_posts), name='feed'),
    path('posts/new/', login_required(create_post), name='create_post'),
]