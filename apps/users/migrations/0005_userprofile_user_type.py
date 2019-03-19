# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-13 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190312_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.IntegerField(choices=[(1, '卖家'), (2, '刷手'), (3, '代理')], default=1, help_text='账号类别: 1(卖家),2(刷手),3(代理)', verbose_name='账号类别'),
        ),
    ]
