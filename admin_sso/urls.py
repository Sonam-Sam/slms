from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PasswordsChangeView

urlpatterns = [

    path('admin_login/', views.loginAdmin, name="admin_login"),
    path('admin_logout/', views.logoutAdmin, name="admin_logout"),

    path('register/', views.registerUser, name="register"),
    path('user-documents/', views.userDocuments, name="user-documents"),

    path('admin-profile/<str:pk>/', views.adminProfile, name="admin-profile"),
    path('admin/', views.adminAccount, name="admin"),
    path('editaccount/', views.editadminAccount, name="editaccount"),

    path('', views.users, name="users"),
    path('profile/<str:pk>/', views.singleProfile, name="single-profile"),

    path('leaverequest/', views.leaveRequest, name="leaverequest"),
    path('leave/<str:pk>/', views.viewLeave, name="leave"),

    path('editUser/<str:pk>/', views.editUser, name="editUser"),
    path('deleteUser/<str:pk>/', views.deleteUser, name="deleteUser"),
    
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='admin_sso/change-password.html')),
    path('admin_password/', PasswordsChangeView.as_view(template_name='admin_sso/change-password.html'), name='admin_password'),
    path('psuccess/', views.psuccess, name='psuccess'),
]