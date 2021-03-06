# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-24 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0008_auto_20180122_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_status',
            field=models.CharField(choices=[('TRADE_SUCCESS', '成功'), ('TRADE_CLOSED', '超时关闭'), ('WAIT_BUYER_PAY', '交易创建'), ('TRADE_FINISHED', '交易结束'), ('paying', '待支付')], default='paying', max_length=20, verbose_name='订单状态'),
        ),
    ]
