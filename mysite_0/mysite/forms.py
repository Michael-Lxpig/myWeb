# coding=utf-8
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType


class loginForms(forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码', widget=forms.PasswordInput)


class RegForms(forms.Form):
    username = forms.CharField(label='用户名', max_length=20, min_length=3)
    password = forms.CharField(label='密码', widget=forms.PasswordInput)
    #reput = forms.CharField(label='请再输入一次密码', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('用户名已经存在')
        return username

    '''def clean_password(self):
        password = self.cleaned_data['password']
        reput = self.cleaned_data['reput']
        if password != reput:
            raise forms.ValidationError('密码两次输入不一致')
        return password'''
