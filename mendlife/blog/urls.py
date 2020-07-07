from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    #API to post a comment
    path('postComment', views.postComment, name="postComment"),
    path('', views.blogHome, name="bloghome"),
    # The below line tells django to redirect to any random string appended in the address as str:slug.
    path('<str:slug>', views.blogPost, name="blogPost"),
]
