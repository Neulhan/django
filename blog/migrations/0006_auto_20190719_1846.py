# Generated by Django 2.2.3 on 2019-07-19 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='anony',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('d', 'draft'), ('p', 'published'), ('w', 'withdraw')], default='d', max_length=1),
            preserve_default=False,
        ),
    ]