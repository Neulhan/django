# blog/models.py
from django.db import models
import re
from django.forms import ValidationError


# Create your models here.
def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise ValidationError("유효하지 않은 입려값입니다")


class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'published'),
        ('w', 'withdraw'),
    )

    title = models.CharField(max_length=100, help_text="포스팅 제목을 입력해 주세요", verbose_name='제목')  # 길이 제한이 있는 문자열
    content = models.TextField()  # 길이 제한이 없는 문자열
    reference = models.CharField(max_length=150, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # DateTimeField 는 자동으로 설정됨
    tags = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=50)
    anony = models.TextField(default=None)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

