from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

from datetime import datetime

from .models import Post
from .forms import PostForm


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('post:feed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
