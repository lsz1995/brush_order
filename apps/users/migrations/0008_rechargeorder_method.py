# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-14 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190313_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='rechargeorder',
            name='method',
            field=models.IntegerField(choices=[(1, '支付宝'), (2, '微信'), (3, '其他')], default=1, help_text='充值类别: 1(支付宝),2(微信),3(其他)', verbose_name='充值类别'),
        ),
    ]
