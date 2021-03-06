# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-08 12:03
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='姓名')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='出生年月')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=6, verbose_name='性别')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='电话')),
                ('qq_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='QQ号码')),
                ('balance', models.FloatField(default=0, null=True, verbose_name='余额')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='RechargeOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.FloatField(verbose_name='充值金额')),
                ('arrival_money', models.FloatField(default=0, verbose_name='到账金额')),
                ('order_number', models.CharField(blank=True, max_length=300, null=True, verbose_name='充值单号')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('state', models.BooleanField(default=False, verbose_name='处理状态')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='充值用户')),
            ],
            options={
                'verbose_name': '充值订单',
                'verbose_name_plural': '充值订单',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_ww', models.CharField(default='', max_length=100, verbose_name='店铺旺旺')),
                ('store_name', models.CharField(default='', max_length=100, verbose_name='店铺名称')),
                ('store_category', models.CharField(default='', max_length=100, verbose_name='店铺类目')),
                ('store_url', models.URLField(max_length=500, verbose_name='店铺链接')),
                ('sender_name', models.CharField(default='', max_length=100, verbose_name='发件人')),
                ('mobile', models.CharField(default='', max_length=11, verbose_name='电话')),
                ('province', models.CharField(default='', max_length=100, verbose_name='省份')),
                ('city', models.CharField(default='', max_length=100, verbose_name='城市')),
                ('district', models.CharField(default='', max_length=100, verbose_name='区域')),
                ('address', models.CharField(default='', max_length=100, verbose_name='详细地址')),
                ('postal_code', models.CharField(default='', max_length=6, verbose_name='邮编')),
                ('image', models.ImageField(upload_to='store_image', verbose_name='卖家中心图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('state', models.BooleanField(default=False, verbose_name='审核状态')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '我的店铺',
                'verbose_name_plural': '我的店铺',
            },
        ),
        migrations.CreateModel(
            name='VerifyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='邀请码')),
                ('mobile', models.CharField(max_length=11, verbose_name='电话')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '邀请码',
                'verbose_name_plural': '邀请码',
            },
        ),
        migrations.CreateModel(
            name='WithdrawOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.FloatField(verbose_name='提现金额')),
                ('Bank_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='提现银行卡号')),
                ('arrival_money', models.FloatField(default=0, verbose_name='到账金额')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('state', models.BooleanField(default=False, verbose_name='处理状态')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='提现用户')),
            ],
            options={
                'verbose_name': '提现订单',
                'verbose_name_plural': '提现订单',
            },
        ),
    ]
