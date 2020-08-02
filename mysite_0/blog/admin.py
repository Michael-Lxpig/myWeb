# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import BlogType
from models import Blog
from django.contrib import admin


# Register your models here.
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog_type', 'author', 'creat_time')


