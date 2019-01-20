from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.db.utils import IntegrityError
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, FormView

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


def update_profile(request):
    profile = request.user.profile
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES )
        if form.is_valid():
            data = form.cleaned_data
            
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            url = reverse('users:detail', kwargs={'username': request.user.username})
            return redirect(url)
    else:
        form = ProfileForm()

    return render(request, 'users/update_profile.html', {
        'profile': profile,
        'user': request.user,
        'form': form
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('post:feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid usersname or password'})
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('users:login')
