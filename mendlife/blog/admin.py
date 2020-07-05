from django.contrib import admin
from blog.models import Post,Tech, BlogComment
# Register your models here.
admin.site.register(BlogComment)

#Add this media to the post while registering it.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ("tinyinject.js",)

@admin.register(Tech)
class TechAdmin(admin.ModelAdmin):
    class Media:
        js = ("tinyinject.js",)