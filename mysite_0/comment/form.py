# coding=utf-8
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from ckeditor.widgets import CKEditorWidget

class CommentForms(forms.Form):
    #object_id=forms.IntegerField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    text = forms.CharField(widget=CKEditorWidget(config_name='custom'))

    def empty(self):
        text = self.cleaned_data.get("text")
        if text=="":
            raise forms.ValidationError("请勿提交空评论")
        return text