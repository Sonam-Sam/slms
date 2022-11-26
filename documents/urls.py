from django.urls import path
from . import views

urlpatterns = [

    # Leave Section
    path('leave/', views.leave, name="leave"),
    path('applyleave/', views.applyLeave, name="applyleave"),
    path('edit-leave/<str:pk>/', views.editLeave, name="edit-leave"),
    path('delete-leave/<str:pk>/', views.deleteLeave, name="delete-leave"),

    # Document Section
    path('documents/', views.documents, name="documents"),
    path('create-document/', views.createDocument, name="create-document"),
    path('update-document/<str:pk>/', views.updateDocument, name="update-document"),
    path('delete-document/<str:pk>/', views.deleteDocument, name="delete-document"),
    
]