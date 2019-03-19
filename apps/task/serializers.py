# -*- coding:utf-8 -*-

import re
from rest_framework import serializers
from django.contrib.auth import get_user_model,get_user
from datetime import datetime
from datetime import timedelta
from rest_framework.validators import UniqueValidator
from users.models import UserProfile
from apps.task.models import BrushTask,OrderInfos,LogisticsTask,LogisticsTaskOrder
from django.db.models import Q

User = get_user_model()



class BrushTaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(#
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')




    def create(self, validated_data):
        user = validated_data['user']

        instance = BrushTask.objects.create(**validated_data)

        price = (instance.single_price+instance.commission)*instance.numbers #订单总价格
        user.balance =user.balance-price #
        user.save()

        return instance
    def validate(self,attrs):  # 验证过程

        if attrs["single_price"]< 0 or attrs['commission']<0:
            raise serializers.ValidationError("本金或佣金不能小于0")

        total = (attrs['single_price']+attrs['commission'])*attrs["numbers"]
        balance = attrs['user'].balance
        if balance < total: #余额不能小于订单总价格
            raise serializers.ValidationError("余额不足")
        else:

            return attrs


    class Meta:
        model = BrushTask
        # fields = ("id", "user", "money", "Bank_number",'arrival_money','add_time')
        fields = "__all__"


class AllBrushTask(serializers.ModelSerializer):
    class Meta:
        model = BrushTask
        # fields = ("id", "user", "money", "Bank_number",'arrival_money','add_time')
        fields = "__all__"


class OrderInfosSerializer(serializers.ModelSerializer):

    #刷手提供订单信息
    user = serializers.HiddenField(#
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    def create(self, validated_data):


        activity = validated_data['activity']

        instance = OrderInfos.objects.create(**validated_data) #创建单个任务订单
        instance.single_price = activity.single_price
        instance.commission = activity.commission
        instance.activity_name = activity.title
        instance.save()

        count =activity.numbers#订单所在任务数量-1
        activity.numbers =count-1
        activity.save()
        return instance

    def validate_activity(self,activity):  # 验证过程


        if activity.numbers<=0:
            raise serializers.ValidationError("任务已被接完")
        else:
            return activity


        # if count>0:
        #     pass
        # else:
        #     raise serializers.ValidationError("任务已被接完")




        # print('sss')
        # mobile_records = User.objects.filter(mobile=mobile)
        # if mobile_records:
        #
        #     raise serializers.ValidationError("电话号码已存在")


    class Meta:
        model = OrderInfos
        fields = "__all__"


class GetOrderInfosSerializer(serializers.ModelSerializer):

    #卖家确认完成订单
    # def validated(self,instance):  # 验证过程
    #     print(instance)
    #     print('sss')
    #
    #     return id
        # total = (attrs['single_price']+attrs['commission'])*attrs["numbers"]
        # balance = attrs['user'].balance
        # if balance <total:
        #     raise serializers.ValidationError("余额不足")
        # else:
        #
        #     return attrs


    def update(self, instance, validated_data):  #完成订单后 分钱



        if instance.state_type ==3:
            raise serializers.ValidationError("已完成订单，无法操作")
        else:
            instance.state_type =validated_data['state_type']
            instance.save()
            user = instance.user#订单完成者
            # activity = instance.activity#活动名称
            # creator = activity.user# 活动发布者
            # print(current_user)
            #卖家才能确认订单的权限还没完成###################################################

            if validated_data['state_type'] == 3:

                print('wancheng')
                if user.Be_Invite_code :#如果确认订单的卖家是被邀请的

                    inviter = UserProfile.objects.get(Invite_code=user.Be_Invite_code) #邀请人
                    print(inviter, '+1')
                    inviter.balance = inviter.balance + 1#邀请人抽成1元
                    inviter.save()
                    user.balance = user.balance + instance.commission -5#订单完成者获得（佣金-5）
                    user.save()
                    print(user, '+',instance.commission -5)
                    return instance
                else:
                    user.balance = user.balance + instance.commission -5
                    user.save()
                    print(user, '+',instance.commission -5)
                    return instance

            return  instance
    class Meta:
        model = OrderInfos
        # fields = ("id", "state_type")
        fields = "__all__"

class LogisticsTaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(#
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')




    # def create(self, validated_data):
    #     user = validated_data['user']
    #
    #     instance = BrushTask.objects.create(**validated_data)
    #
    #     price = (instance.single_price+instance.commission)*instance.numbers #订单总价格
    #     user.balance =user.balance-price #
    #     user.save()
    #
    #     return instance
    # def validate(self,attrs):  # 验证过程
    #
    #     if attrs["single_price"]< 0 or attrs['commission']<0:
    #         raise serializers.ValidationError("本金或佣金不能小于0")
    #
    #     total = (attrs['single_price']+attrs['commission'])*attrs["numbers"]
    #     balance = attrs['user'].balance
    #     if balance < total: #余额不能小于订单总价格
    #         raise serializers.ValidationError("余额不足")
    #     else:
    #
    #         return attrs


    class Meta:
        model = LogisticsTask
        # fields = ("id", "user", "money", "Bank_number",'arrival_money','add_time')
        fields = "__all__"