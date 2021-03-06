from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import LoginView, LogoutView
from .views import Signup, UserDetailView, UpdateProfileView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', Signup.as_view(), name='signup'),
    path('me/profile', UpdateProfileView.as_view(), name='update_profile'),
    path('<str:username>/', UserDetailView.as_view(), name='detail'),
]