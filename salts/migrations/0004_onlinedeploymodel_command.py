# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-19 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salts', '0003_onlinedeploymodel_deploy_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinedeploymodel',
            name='command',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
