from django.urls import re_path, path
from . import views


urlpatterns = [
    re_path(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.mysum)
]
