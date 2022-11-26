from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import *
from documents.models import Document, Profile
from users.models import Profile as pp
from .utils import searchProfiles, searchDocuments, paginateDocuments, paginateProfiles
from django.views import generic
from django.db.models import Q
from . models import ssoProfile
from django.urls import reverse_lazy
from documents.models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm


def adminProfile(request, pk):
    profile = ssoProfile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'admin_sso/single-profile.html', context)

@login_required(login_url='admin_login')
def adminAccount(request):
    profile = pp.objects.all()
    context = {'profile': profile}
    return render(request, 'admin_sso/admin.html', context)

@login_required(login_url='admin_login')
def editadminAccount(request):
    profile = request.user.profile
    # profile = ssoProfile.objects.all()
    form = AdminForm(instance=profile)

    if request.method == 'POST':
        form = AdminForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('admin')

    context = {'form': form, 'profile':profile}
    return render(request, 'admin_sso/a_form.html', context)

# Create your views here.
@login_required(login_url="admin_login")
def registerUser(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            # form.save()

            messages.success(request, 'User was successfully registered! ')

            return redirect('users')

        else:
            messages.error(request, 'An error occurred registering the User!')

    context = {'form': form}
    return render(request, 'admin_sso/addUser.html', context)


def loginAdmin(request):
    if request.user.is_authenticated:
        return redirect('users')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Admin with this username does not exist!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if(((username == User.objects.get(username=username)) and (password == User.objects.get(password=password)))):
                return redirect('users')
            else:

                messages.error(request, 'Username OR Password is incorrect!')
        else:
            messages.error(request, 'Username OR Password is incorrect!')

    return render(request, 'admin_sso/admin_login.html')

def logoutAdmin(request):
    logout(request)
    messages.info(request, 'Admin was logged out successfully!')
    return render(request, 'admin_sso/admin_login.html')

@login_required(login_url="admin_login")
def leaveRequest(request):
    leaverequest = Leave.objects.all()
    unreadCount = leaverequest.filter(status='Pending').count()
    context = {'leaverequest': leaverequest, 'unreadCount': unreadCount}

    return render(request, 'admin_sso/leaverequest.html', context)

@login_required(login_url="admin_login")
def viewLeave(request, pk):
    leaver = Leave.objects.get(id=pk)
    profile = Profile.objects.all()
    context = {'leaver': leaver}
    
    if request.method == 'POST':

        mess = 'Hurry Up! Your leave request has been made changes by student service officer and see your status.'
        to_email = leaver.student.email

        send_mail(
                "Leave Request Action",
                mess,
                settings.EMAIL_HOST_USER,
                [to_email], 
                fail_silently=False,
            )

        x = request.POST.get('radio')
        
        Leave.objects.filter(id = pk).update(status = x)

        return redirect('leaverequest')

    return render(request, 'admin_sso/leaveDetails.html', context)

@login_required(login_url="admin_login")
def userDocuments(request):
    
    documents, search_query = searchDocuments(request)

    custom_range, documents = paginateDocuments(request, documents, 9)

    context = {'documents': documents, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'admin_sso/user-documents.html', context)

@login_required(login_url="admin_login")
def users(request):
    profiles, search_query = searchProfiles(request)

    custom_range, profiles = paginateProfiles(request, profiles, 6)

    context = {'profiles': profiles, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'admin_sso/users.html', context)

@login_required(login_url="admin_login")
def singleProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'admin_sso/single-profile.html', context)

@login_required(login_url="admin_login")
def editUser(request, pk):
    profile = Profile.objects.get(id=pk)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('users')

    context = {'form': form}
    return render(request, 'admin_sso/p_form.html', context)

@login_required(login_url="admin_login")
def deleteUser(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('users')

    context = {'object':profile}
    return render(request, 'admin_sso/delete_template.html', context)

class PasswordsChangeView(PasswordChangeView):
    form_class = PChangeForm
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('psuccess')

def psuccess(request):
    return redirect(request, 'admin_sso/password_success.html', {})