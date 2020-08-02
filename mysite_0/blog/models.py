# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class BlogType(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return "%s" % self.type


class Blog(models.Model):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    context = RichTextUploadingField()
    author = models.ForeignKey(User)
    creat_time = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
        #return self.title
