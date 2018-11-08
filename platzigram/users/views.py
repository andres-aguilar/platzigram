from django.shortcuts import render

from django.db.utils import IntegrityError
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import Profile
from .forms import ProfileForm, SignupForm

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

            return redirect('users:update_profile')
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


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()

    return render(
        request=request,
        template_name='users/signup.html',
        context={'form': form}
    )