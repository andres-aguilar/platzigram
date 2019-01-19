from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

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


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post:feed')
    else:
        form = PostForm()

    return render(request, 'posts/new.html',  {
        'form': form,
        'user': request.user,
        'profile': request.user.profile
        }
    )