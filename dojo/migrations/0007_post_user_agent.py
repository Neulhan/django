# Generated by Django 2.2.3 on 2019-08-02 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0006_auto_20190802_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_agent',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
