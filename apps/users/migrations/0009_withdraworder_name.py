# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-14 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rechargeorder_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdraworder',
            name='name',
            field=models.CharField(default='', max_length=6, verbose_name='银行卡持有人姓名'),
        ),
    ]