from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('postComment', views.postComment, name="postComment"),
    path('', views.wHome, name="wHome"),
    # The below line tells django to redirect to any random string appended in the address as str:slug.
    path('<str:slug>', views.wPost, name="wPost"),
]
