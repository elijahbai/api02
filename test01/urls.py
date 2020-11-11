from django.conf.urls import url, include
from test01 import views

urlpatterns = [
    url(r'add_person$', views.add_person, ),
    url(r'show_persons$', views.show_persons, ),
    url(r'my/api$', views.my_api, ),
    url(r'post$', views.post, ),
]