from django.contrib import admin

# Register your models here.
from .models import Tweet, Like
admin.site.register(Tweet)
admin.site.register(Like)
