# blog/models.py
from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100,help_text="포스팅 제목을 입력해 주세요", verbose_name='제목')  # 길이 제한이 있는 문자열
    content = models.TextField()  # 길이 제한이 없는 문자열
    reference = models.CharField(max_length=150, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # DateTimeField 는 자동으로 설정됨
