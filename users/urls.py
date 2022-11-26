from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PasswordsChangeView

urlpatterns = [
    path('', views.index, name="index"),
    path('index_nav', views.index_nav, name="index_nav"),

    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('profiles/', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('sso/', views.sso, name="sso"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('contact_us_nav/', views.contact_us_nav, name="contact_us_nav"),

    path('account/', views.userAccount, name="account"),
    path('edit-account/', views.editAccount, name="edit-account"),

    path('password/', PasswordsChangeView.as_view(template_name = 'users/changepass.html'), name="password"),
    path('password_success/', views.password_success, name="password_success")
]