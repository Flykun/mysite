from django.contrib import admin

from .models import BlogType, Blog

admin.site.register(BlogType)
admin.site.register(Blog)
