from django.urls import re_path, path
from . import views


urlpatterns = [
    path('sum/<str:x>/<int:y>/', views.mysum)
]
