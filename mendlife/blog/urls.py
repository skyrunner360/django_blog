from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.blogHome, name="bloghome"),
    # The below line tells django to redirect to any random string appended in the address as str:slug.
    path('<str:slug>', views.blogPost, name="blogPost"),
]
