# Generated by Django 2.2.3 on 2019-08-02 02:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0005_auto_20190802_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameuser',
            name='username',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]