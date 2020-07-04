from django.contrib import admin
from writings.models import Writing, WComment
# Register your models here.
admin.site.register((Writing,WComment))