# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20170124_1757'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='alias',
            field=models.CharField(default='anonymous', max_length=255),
        ),
    ]
