"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

from django.contrib.auth.decorators import login_required

from post.views import list_posts, create_post
from users.views import login_view, logout_view, signup_view, update_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    # Post views
    path('', login_required(list_posts), name='feed'),
    path('posts/new/', login_required(create_post), name='create_post'),
    # User views
    path('users/login', login_view, name='login'),
    path('users/logout', login_required(logout_view), name='logout'),
    path('users/signup', signup_view, name='signup'),
    path('users/me/profile', login_required(update_profile), name='update_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
