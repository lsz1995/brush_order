# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-12 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190312_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='image',
            field=models.ImageField(blank=True, default='store_image/default', null=True, upload_to='store_image', verbose_name='卖家中心图片'),
        ),
    ]
