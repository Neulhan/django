from django.db import models
from django import forms
from django.core.validators import MinLengthValidator as MLV


# Create your models here.


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요')


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_length_3_validator])
    content = models.TextField()
    ip = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GameUser(models.Model):
    server_name = models.CharField(max_length=10,
                                   choices=(
                                       ('A', 'A서버'),
                                       ('B', 'B서버'),
                                       ('C', 'C서버'),

                                   ))
    username = models.CharField(max_length=20, validators=[MLV(3)])

    class Meta:
        unique_together = [
            ('server_name', 'username'),
        ]
