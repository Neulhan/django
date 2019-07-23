# blog/models.py
from django.db import models
import re
from django.forms import ValidationError
from django.contrib.auth.models import User

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
    author = models.CharField(max_length=50)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return str(self.name)

class Profile(models.Model):
    pass