# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-13 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20190310_1903'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brushtask',
            options={'verbose_name': '刷单活动', 'verbose_name_plural': '刷单活动'},
        ),
        migrations.AddField(
            model_name='brushtask',
            name='commission',
            field=models.FloatField(default=0, verbose_name='佣金'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='is_consulting_service',
            field=models.BooleanField(default=False, verbose_name='是否咨询客服'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='price_minimum',
            field=models.FloatField(verbose_name='最低价格'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='single_price',
            field=models.FloatField(default=0, verbose_name='本金'),
        ),
    ]