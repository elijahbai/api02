"""api02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include,re_path
from django.contrib import admin
from django.urls import path


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^my/api$',views.my_api,name='my_api'),
    # url(r'^articles$',views.add_article,name='add_article'),
    # url(r'^articles/<int:art_id>$',views.modify_article,name='modify_article'),
    # url(r'add_person$', views.add_person, ),
    # url(r'show_persons$', views.show_persons, ),
    path('admin/', admin.site.urls),
    # url(r'^api/', include(myapp.urls)),
    re_path('^api/(?P<version>\w+)/user/',include('api.user.urls')),
    re_path('^api/(?P<version>\w+)/message/',include('api.message.urls')),
]
