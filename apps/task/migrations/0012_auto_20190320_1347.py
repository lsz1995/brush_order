# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-20 13:47
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0011_auto_20190319_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='logisticstask',
            name='Courier_number',
            field=models.CharField(blank=True, default='', help_text='快递单号', max_length=100, verbose_name='快递单号'),
        ),
        migrations.AddField(
            model_name='logisticstask',
            name='content',
            field=models.TextField(blank=True, default='', help_text='物流信息', verbose_name='物流信息'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='activity_entrance',
            field=models.CharField(help_text='活动入口', max_length=100, verbose_name='活动入口'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='activity_interval',
            field=models.CharField(help_text='活动间隔', max_length=200, verbose_name='活动间隔'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='activity_keyword',
            field=models.CharField(help_text='进店关键字', max_length=100, verbose_name='进店关键字'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='activity_platform',
            field=models.CharField(help_text='活动平台', max_length=100, verbose_name='活动平台'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='activity_sku',
            field=models.CharField(help_text='活动SKU选项', max_length=100, verbose_name='活动SKU选项'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='added_message',
            field=models.CharField(help_text='补充说明', max_length=500, verbose_name='补充说明'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='allow_pay',
            field=models.CharField(help_text='允许付款方式（用逗号隔开）', max_length=200, verbose_name='允许付款方式（用逗号隔开）'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='before_activity',
            field=models.CharField(help_text='活动前', max_length=100, verbose_name='活动前'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='client_type',
            field=models.CharField(help_text='客户端类型', max_length=50, verbose_name='客户端类型'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='commission',
            field=models.FloatField(default=0, help_text='佣金', verbose_name='佣金'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='delivery_place',
            field=models.CharField(help_text='发货地', max_length=100, verbose_name='发货地'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='evaluation',
            field=models.CharField(help_text='产品自评', max_length=200, verbose_name='产品自评'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='image',
            field=models.ImageField(blank=True, help_text='活动图片', upload_to='activity_image', verbose_name='活动图片'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='is_consulting_service',
            field=models.BooleanField(default=False, help_text='是否咨询客服', verbose_name='是否咨询客服'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='is_photo',
            field=models.BooleanField(default=False, help_text='是否实拍', verbose_name='是否实拍'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='numbers',
            field=models.IntegerField(default=0, help_text='刷单次数', verbose_name='刷单次数'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='order_message',
            field=models.CharField(help_text='网店订单留言', max_length=100, verbose_name='网店订单留言'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='order_payment_time',
            field=models.CharField(help_text='下单付款时间', max_length=100, verbose_name='下单付款时间'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='price_highest',
            field=models.FloatField(help_text='最高价格', verbose_name='最高价格'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='price_minimum',
            field=models.FloatField(help_text='最低价格', verbose_name='最低价格'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='product_url',
            field=models.CharField(help_text='产品链接', max_length=500, verbose_name='产品链接'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='search_rank',
            field=models.CharField(help_text='搜索排序', max_length=100, verbose_name='搜索排序'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='single_price',
            field=models.FloatField(default=0, help_text='本金', max_length=600, verbose_name='本金'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='state',
            field=models.BooleanField(default=True, help_text='活动状态', verbose_name='活动状态'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='store_name',
            field=models.CharField(help_text='店铺名称', max_length=50, verbose_name='店铺名称'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='store_ww',
            field=models.CharField(help_text='店铺旺旺', max_length=50, verbose_name='店铺旺旺'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='style',
            field=models.CharField(help_text='款式', max_length=100, verbose_name='款式'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='title',
            field=models.CharField(help_text='活动标题', max_length=300, verbose_name='活动标题'),
        ),
        migrations.AlterField(
            model_name='brushtask',
            name='user',
            field=models.ForeignKey(help_text='刷单任务发布者', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='刷单任务发布者'),
        ),
        migrations.AlterField(
            model_name='logisticstask',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='logisticstask',
            name='address',
            field=models.CharField(default='', help_text='详细地址', max_length=100, verbose_name='详细地址'),
        ),
        migrations.AlterField(
            model_name='logisticstask',
            name='city',
            field=models.CharField(default='', help_text='城市', max_length=100, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='logisticstask',
            name='commission',
            field=models.FloatField(default=0, help_text='佣金', verbose_name='佣金'),
        ),
        migrations.AlterField(
            model_name='logisticstask',
            name='district',
            field=models.CharField(default='', help_text='区域', max_length=100, verbose_name='区域'),
        ),
        migrations.AlterField(
            model_name='logisticstask',
            name='mobile',
            field=models.CharField(default='', help_text='收货人电话', max_length=11, verbose_name='收货人电话'),
        ),
        migrations.AlterField(
            model_name='logisticstask',
            name='postal_code',
            field=models.CharField(default='', help_text='邮编', max_length=6, verbose_name='邮编'),
        ),
        migrations.AlterField(
            model_name='logisticstask',
            name='province',
            field=models.CharField(default='', help_text='省份', max_length=100, verbose_name='省份'),
        ),
        migrations.AlterField(
            model_name='logisticstask',
            name='receive_name',
            field=models.CharField(default='', help_text='收货人', max_length=100, verbose_name='收货人'),
        ),
        migrations.AlterField(
            model_name='logisticstask',
            name='state',
            field=models.BooleanField(default=False, help_text='任务被接状态', verbose_name='任务被接状态'),
        ),
        migrations.AlterField(
            model_name='logisticstask',
            name='user',
            field=models.ForeignKey(help_text='任务发布者', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='任务发布者'),
        ),
        migrations.AlterField(
            model_name='logisticstaskorder',
            name='Courier_number',
            field=models.CharField(blank=True, default='', help_text='快递单号', max_length=100, verbose_name='快递单号'),
        ),
        migrations.AlterField(
            model_name='logisticstaskorder',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='logisticstaskorder',
            name='commission',
            field=models.FloatField(default=0, help_text='佣金', verbose_name='佣金'),
        ),
        migrations.AlterField(
            model_name='logisticstaskorder',
            name='mobile',
            field=models.CharField(default='', help_text='收货人电话', max_length=11, verbose_name='收货人电话'),
        ),
        migrations.AlterField(
            model_name='logisticstaskorder',
            name='receive_name',
            field=models.CharField(default='', help_text='收货人', max_length=100, verbose_name='收货人'),
        ),
        migrations.AlterField(
            model_name='logisticstaskorder',
            name='state',
            field=models.BooleanField(default=False, help_text='任务状态', verbose_name='任务状态'),
        ),
        migrations.AlterField(
            model_name='logisticstaskorder',
            name='task',
            field=models.ForeignKey(help_text='所接物流任务', on_delete=django.db.models.deletion.CASCADE, to='task.LogisticsTask', verbose_name='所接物流任务'),
        ),
        migrations.AlterField(
            model_name='logisticstaskorder',
            name='user',
            field=models.ForeignKey(help_text='接受任务者', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='接受任务者'),
        ),
        migrations.AlterField(
            model_name='orderinfos',
            name='Courier',
            field=models.CharField(blank=True, default='', help_text='什么快递', max_length=100, verbose_name='快递'),
        ),
        migrations.AlterField(
            model_name='orderinfos',
            name='Courier_number',
            field=models.CharField(blank=True, default='', help_text='快递单号', max_length=100, verbose_name='快递单号'),
        ),
        migrations.AlterField(
            model_name='orderinfos',
            name='activity',
            field=models.ForeignKey(help_text='所接任务', on_delete=django.db.models.deletion.CASCADE, to='task.BrushTask', verbose_name='所接任务'),
        ),
        migrations.AlterField(
            model_name='orderinfos',
            name='activity_name',
            field=models.CharField(default='', help_text='活动名称', max_length=500, verbose_name='活动名称'),
        ),
        migrations.AlterField(
            model_name='orderinfos',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='接单时间', verbose_name='接单时间'),
        ),
        migrations.AlterField(
            model_name='orderinfos',
            name='buyer',
            field=models.CharField(blank=True, default='', help_text='买家', max_length=100, verbose_name='买家'),
        ),
        migrations.AlterField(
            model_name='orderinfos',
            name='commission',
            field=models.FloatField(default=0, help_text='佣金（平台共收多少钱）', verbose_name='佣金'),
        ),
        migrations.AlterField(
            model_name='orderinfos',
            name='order',
            field=models.CharField(blank=True, default='', help_text='订单号', max_length=100, verbose_name='订单号'),
        ),
        migrations.AlterField(
            model_name='orderinfos',
            name='single_price',
            field=models.FloatField(default=0, help_text='本金（商品价格）', verbose_name='本金'),
        ),
        migrations.AlterField(
            model_name='orderinfos',
            name='user',
            field=models.ForeignKey(help_text='接单人', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='接单人'),
        ),
    ]
