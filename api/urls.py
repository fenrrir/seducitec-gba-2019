from django.urls import path

from . import views

urlpatterns = [
    path('users-list/', views.ListUsers.as_view())
]
