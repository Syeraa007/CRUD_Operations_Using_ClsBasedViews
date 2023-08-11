"""
URL configuration for CRUD_Operations project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # Static URL Suffixes(Normal URLs)
    path('TopicList/',TopicList.as_view(),name='TopicList'),
    path('WebpageList/',WebpageList.as_view(),name='WebpageList'),
    path('TopicCreate/',TopicCreate.as_view(),name='TopicCreate'),
    path('WebpageCreate/',WebpageCreate.as_view(),name='WebpageCreate'),

    # Dynamic URL Suffixes(Canonical URLs)
    re_path('^update/(?P<pk>\d+)/',TopicUpdate.as_view(),name='TopicUpdate'),
    re_path('^update/(?P<name>\d+)/',WebpageUpdate.as_view(),name='WebpageUpdate'),
    re_path('^delete/(?P<pk>\d+)/',TopicDelete.as_view(),name='TopicDelete'),
    re_path('(?P<pk>\d+)/',TopicDetail.as_view(),name='TopicDetail'),
    re_path('(?P<name>\d+)/',WebpageDetail.as_view(),name='WebpageDetail'),
]
