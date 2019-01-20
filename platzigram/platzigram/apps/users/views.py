from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.db.utils import IntegrityError
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views 
from django.views.generic import TemplateView, DetailView, FormView, UpdateView

from platzigram.apps.post.models import Post

from .models import Profile
from .forms import ProfileForm, SignupForm

from django.contrib.auth.models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class Signup(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/update_profile.html'
    model = Profile 
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        return self.request.user.profile

    def get_success_url(self):
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': self.request.user.username})


class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'


def logout_view(request):
    logout(request)
    return redirect('users:login')
