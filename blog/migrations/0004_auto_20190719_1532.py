# Generated by Django 2.2.3 on 2019-07-19 06:32

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190719_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='lnglat',
            field=models.CharField(blank=True, help_text='위도,경도 포맷으로 입력', max_length=50, validators=[blog.models.lnglat_validator]),
        ),
    ]