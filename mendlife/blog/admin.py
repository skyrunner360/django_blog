from django.contrib import admin
from blog.models import Post,Tech, BlogComment
# Register your models here.
admin.site.register((Post, Tech, BlogComment))