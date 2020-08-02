from django.conf.urls import url
from comment import views
from django.contrib import admin

urlpatterns = [
       url(r'^comment/',views.update_comment ,name="update_comment")
    ]