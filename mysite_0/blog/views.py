# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Blog, BlogType
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from mysite.forms import loginForms, RegForms
from comment.models import Comment
from comment.form import CommentForms


# Create your views here.
def blog_list(request):
    articles = Blog.objects.all()
    blog_types = BlogType.objects.all()
    context = {'articles': articles, 'blog_types': blog_types}
    return render(request, 'blog_list.html', context)


def blog_detail(request, blog_pk):
    article = get_object_or_404(Blog, id=blog_pk)
    # id = request.POST.get('blog_id')
    blog_content_type = ContentType.objects.get_for_model(Blog)
    comments = Comment.objects.filter(object_id=blog_pk)

    context = {'article': article, 'user': request.user, 'comments': comments,
               'form': CommentForms(initial={'object_id': blog_pk})}
    return render(request, 'blog_detail.html', context)


def home(request):
    return render(request, 'home.html')


def user_login(request):
    login_form = loginForms(request.POST)
    if request.method == 'POST':
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect(reverse('home'))
            else:
                login_form.add_error(None, '用户名或密码错误')
                return render(request, 'login.html', {'form': login_form})
    else:
        login_form = loginForms()
    form = loginForms()
    context = {'form': form}
    return render(request, 'login.html', context)


def user_logout(request):
    auth.logout(request)
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    return redirect(referer)


def user_register(request):
    if request.method == 'POST':
        reg_form = RegForms(request.POST)
        if reg_form.is_valid():
            # 注册
            username = reg_form.cleaned_data['username']
            password = reg_form.cleaned_data['password']
            user = User.objects.create_user(username,"",password)
            user.save()
            # 登录
            user = auth.authenticate(username=username, password=password)
            return render(request, 'register_ok.html')
    else:
        reg_form = RegForms()
    context = {'form': reg_form}
    return render(request, 'register.html', context)


def django_list(request, type_pk):
    articles = Blog.objects.filter(blog_type_id=type_pk)
    blog_types = BlogType.objects.all()
    return render(request, 'list_by_type.html', {'articles': articles, 'blog_types': blog_types})
