from django.shortcuts import render, redirect

from datetime import datetime

from .models import Post
from .forms import PostForm


def list_posts(request):
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts': posts})


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