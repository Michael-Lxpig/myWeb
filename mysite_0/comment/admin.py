# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Comment
from django.contrib import admin


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('object_id', 'comment_time', 'text', 'user')
