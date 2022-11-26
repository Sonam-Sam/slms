from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from documents.models import Document, Leave
from users.models import Profile
from .models import ssoProfile
from django import forms

class AdminForm(ModelForm):
    class Meta:
        model = ssoProfile
        fields = ['name', 'username', 'email', 'gender', 'profile_image']

    def __init__(self, *args, **kwargs):
        super(AdminForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']

        labels = {
            'first_name': 'Name', 'email': 'Email', 'username': 'Student ID'
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update(
            {'class': 'input'})

        self.fields['email'].widget.attrs.update(
            {'class': 'input'})

        self.fields['username'].widget.attrs.update(
            {'class': 'input'})

        self.fields['password1'].widget.attrs.update(
            {'class': 'input'})

        self.fields['password2'].widget.attrs.update(
            {'class': 'input'})


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'description', 'featured_image']

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'})

        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Short description'})

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'year', 'semester', 'course', 'gender']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

# Leave Section
class LeaveForm(ModelForm):
    class Meta:
        model = Leave
        fields = ['student', 'leave', 'startdate', 'enddate', 'reason']

    def __init__(self, *args, **kwargs):
        super(LeaveForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class PChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

        labels = {
            'old_password': 'Old Password', 'new_password1': 'New Password', 'new_password2': 'Repeat New Password'
        }

    def __init__(self, *args, **kwargs):
        super(PChangeForm, self).__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs.update(
            {'class': 'input'})

        self.fields['new_password1'].widget.attrs.update(
            {'class': 'input'})

        self.fields['new_password2'].widget.attrs.update(
            {'class': 'input'})
