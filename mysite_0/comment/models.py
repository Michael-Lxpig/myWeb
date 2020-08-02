# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Comment(models.Model):
    object_id = models.PositiveIntegerField()
    text= models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
