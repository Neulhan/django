from django.urls import re_path, path
from . import views
from . import views_cbv


urlpatterns = [
    re_path(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.mysum),
    re_path(r'^list1/$', views.post_list1),
    re_path(r'^list2/$', views.post_list2),
    re_path(r'^list3/$', views.post_list3),
    re_path(r'^excel/$', views.excel_download),
]
