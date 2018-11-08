from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import login_view, logout_view, signup_view, update_profile

urlpatterns = [
    path('login', login_view, name='login'),
    path('logout', login_required(logout_view), name='logout'),
    path('signup', signup_view, name='signup'),
    path('me/profile', login_required(update_profile), name='update_profile'),
]