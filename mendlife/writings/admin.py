from django.contrib import admin
from writings.models import Writing, WComment
# Register your models here.
admin.site.register(WComment)

@admin.register(Writing)
class WriteAdmin(admin.ModelAdmin):
    class Media:
        js = ("tinyinject.js",)