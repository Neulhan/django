from django.urls import re_path, path
from . import views
from . import views_cbv


urlpatterns = [
    re_path(r'^new/$', views.post_new),
    re_path(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.mysum),
]
