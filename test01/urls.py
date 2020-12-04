from django.conf.urls import url, include
from test01 import views
from django.urls import path,re_path
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'add_person$', views.add_person, ),
    url(r'show_persons$', views.show_persons, ),
    url(r'my/api$', views.my_api, ),
    url(r'post$', views.post, ),
    path('user/', UserView.as_view()),
    re_path('user/(?P<pk>\d+)/$', UserView.as_view()),
]