from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from . models import Profile
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.conf import settings
from .forms import ProfileForm, PasswordForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('documents')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if(((username == 'admin') and (password == 'adminsso123'))):
                messages.error(request, 'Username OR Password is incorrect!')
                return render(request, 'users/login_register.html')

            elif(((username == User.objects.get(username=username)) and (password == User.objects.get(password=password)))):
                return redirect('documents') 
                
            else:
                messages.error(request, 'Username OR Password is incorrect!')
    
        else:
            messages.error(request, 'Username OR Password is incorrect!')

    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out successfully!')
    return redirect('login')


# Create your views here.
def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'users/user-profile.html', context)


def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def index_nav(request):
    return render(request, 'index_nav.html')

def sso(request):
    return render(request, 'sso.html')

def contact_us(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('message')

        send_mail(
            name,
            content,
            settings.EMAIL_HOST_USER,
            [email, '12190024.gcit@rub.edu.bt', 'sonam12190024@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, 'Message sent successfully! ')

        return render(request, 'contact_us.html', {'email': email})

    else:
        messages.error(request, 'Error sending message!')
        return render(request, 'contact_us.html', {})

@login_required(login_url='login')
def contact_us_nav(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('message')

        send_mail(
            name,
            content,
            settings.EMAIL_HOST_USER,
            [email, '12190024.gcit@rub.edu.bt', '12190021.gcit@rub.edu.bt'],
            fail_silently=False,
        )
        messages.success(request, 'Message sent successfully! ')

        return render(request, 'contact_us_nav.html', {'email': email})

    else:
        messages.error(request, 'Error sending message!')
        return render(request, 'contact_us_nav.html', {})

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    context = {'profile': profile}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form}
    return render(request, 'users/profile_form.html', context)

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordForm
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'users/password_success.html', {})