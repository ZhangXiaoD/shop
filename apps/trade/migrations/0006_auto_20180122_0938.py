# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-22 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0005_auto_20180119_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='post_script',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='订单留言'),
        ),
    ]
