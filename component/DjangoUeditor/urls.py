# coding:utf-8
from django import VERSION
from DjangoUeditor.views import get_ueditor_controller

if VERSION[0:2] > (1, 3) and VERSION[0:2] < (2, 0):
    from django.conf.urls import patterns, url

    urlpatterns = patterns('',
                           url(r'^controller/$', get_ueditor_controller)
                           )
elif VERSION[0:2] > (2, 0):
    from django.urls import path, include, re_path

    urlpatterns = [
                   path('controller/', get_ueditor_controller),
                   ]
else:
    from django.conf.urls.defaults import patterns, url

    urlpatterns = patterns('',
                           url(r'^controller/$', get_ueditor_controller)
                           )
