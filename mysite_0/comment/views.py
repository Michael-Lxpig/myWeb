# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Comment
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your views here.
def update_comment(request):
    user = request.user
    text = request.POST.get('text')
    id = request.POST.get('object_id')
    context = {'user': user, 'text': text, 'id': id}
    # return render(request,'login.html',context)
    if(text==""):
        referer = request.META.get('HTTP_REFERER', reverse('home'))
        return redirect(referer,{'warning':"请勿提交空评论"})
    else:
        comment = Comment.objects.create(user=user, text=text, object_id=id)
        comment.save()
        referer = request.META.get('HTTP_REFERER', reverse('home'))
        return redirect(referer,{'warning':""})
