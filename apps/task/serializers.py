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
        instance.state =True

        price = (instance.single_price+instance.commission)*instance.numbers #订单总价格
        user.balance =user.balance-price #
        user.save()
        instance.save()
        print(user,'余额减去',price)

        return instance
    def validate(self,attrs):  # 验证过程
        try:
            if attrs["single_price"]< 0 or attrs['commission']<0:
                raise serializers.ValidationError("本金或佣金不能小于0")

            total = (attrs['single_price']+attrs['commission'])*attrs["numbers"]
            balance = attrs['user'].balance
            if balance < total: #余额不能小于订单总价格
                raise serializers.ValidationError("余额不足")
            else:

                return attrs
        except:
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
# class AllLogisticsTask(serializers.ModelSerializer):
#     class Meta:
#         model = LogisticsTask
#         # fields = ("id", "user", "moneLogisticsTaskSerializery", "Bank_number",'arrival_money','add_time')
#         fields = "__all__"

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
        elif not activity.state:
            raise serializers.ValidationError("任务已被关闭")
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


            if validated_data['state_type'] == 3:

                print('wancheng')
                if user.Be_Invite_code :#如果确认订单的卖家是被邀请的

                    inviter = UserProfile.objects.get(Invite_code=user.Be_Invite_code) #邀请人
                    print(inviter, '+1')
                    inviter.balance = inviter.balance + 1#邀请人抽成1元 （刷手邀请者）加钱
                    inviter.save()
                    user.balance = user.balance + instance.commission -5#订单完成者获得（佣金-5）#刷手加钱
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

# class LogisticsTaskSerializer(serializers.ModelSerializer):
#     user = serializers.HiddenField(#
#         default=serializers.CurrentUserDefault()
#     )
#     add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
#
#
#
#
#     def create(self, validated_data):
#         user = validated_data['user']
#
#         instance = LogisticsTask.objects.create(**validated_data)
#         instance.state =False#物流任务状态默认为未被人接受 ，只允许刷手接单是改变
#         instance.save()
#         price = instance.commission# 刷单价格
#
#
#         user.balance =user.balance-price #发布成功 减去用户余额
#         user.save()
#
#         return instance
#     def validate(self,attrs):  # 验证过程
#
#         if attrs['commission']<0:
#             raise serializers.ValidationError("佣金不能小于0")
#
#         total = attrs['commission']
#         balance = attrs['user'].balance
#         if balance < total: #余额不能小于订单总价格
#             raise serializers.ValidationError("余额不足")
#         else:
#
#             return attrs
#
#
#     class Meta:
#         model = LogisticsTask
#         # fields = ("id", "user", "money", "Bank_number",'arrival_money','add_time')
#         fields = "__all__"
#
#
# class MyLogisticsTaskInfoSerializer(serializers.ModelSerializer):
#
#     #刷手接受和修改物流任务
#     user = serializers.HiddenField(#
#         default=serializers.CurrentUserDefault()
#     )
#     add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
#
#     def create(self, validated_data):
#
#
#         task = validated_data['task']
#
#         instance = LogisticsTaskOrder.objects.create(**validated_data) #创建单个任务订单
#         instance.commission = task.commission
#         instance.receive_name = task.receive_name
#         instance.mobile =task.mobile
#         instance.state =False
#         instance.save()
#         task.state =True
#         task.save()
#         return instance
#
#     def update(self, instance, validated_data):
#
#         instance.Courier_number = validated_data['Courier_number']
#
#         instance.content =validated_data['content']
#         instance.save()
#
#         return instance
#
#
#     def validate_task(self,task):  # 验证过程
#
#
#         if task.state==True:
#             raise serializers.ValidationError("任务已被接")
#         else:
#             return task
#
#
#
#     def validate(self, attrs):
#
#
#         try:
#             state =attrs['state']
#
#         except :
#             state =False
#
#         if state:
#             raise serializers.ValidationError("没有权限确认物流订单")
#
#         return attrs
#
#         # if count>0:
#         #     pass
#         # else:
#         #     raise serializers.ValidationError("任务已被接完")
#
#
#
#
#         # print('sss')
#         # mobile_records = User.objects.filter(mobile=mobile)
#         # if mobile_records:
#         #
#         #     raise serializers.ValidationError("电话号码已存在")
#
#
#     class Meta:
#         model = LogisticsTaskOrder
#         fields = "__all__"
# class LogisticsTaskSureSerializer(serializers.ModelSerializer):
#
#     #卖家确认完成物流订单
#     # def validated(self,instance):  # 验证过程
#     #     print(instance)
#     #     print('sss')
#     #
#     #     return id
#     #     total = (attrs['single_price']+attrs['commission'])*attrs["numbers"]
#     #     balance = attrs['user'].balance
#     #     if balance <total:
#     #         raise serializers.ValidationError("余额不足")
#     #     else:
#     #
#     #         return attrs
#
#
#     def update(self, instance, validated_data):  #完成物流订单后 分钱
#
#
#         #只允许更改订单状态
#         if instance.state == True:
#             raise serializers.ValidationError("已完成订单，无法操作")
#         else:
#             instance.state =validated_data['state']
#             instance.save()
#             user = instance.user#订单完成者（刷手）
#
#             # activity = instance.activity#活动名称
#             # creator = activity.user# 活动发布者
#             # print(current_user)
#             #卖家才能确认订单的权限还没完成###################################################
#
#             if validated_data['state'] == True:
#                 #给刷手加钱
#                 user.balance +=instance.commission
#                 print('刷手加钱',instance.commission)
#                 user.save()
#                 #给刷手的邀请者加钱
#
#                 pass
#
#
#             return  instance
#     class Meta:
#         model = LogisticsTaskOrder
#         # fields = ("id", "state_type")
#         fields = "__all__"

class LogisticsTaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(#
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')




    def create(self, validated_data):
        user = validated_data['user']

        instance = LogisticsTask.objects.create(**validated_data)
        instance.state =False#物流任务状态默认为未被人接受 ，只允许刷手接单是改变
        instance.save()
        price = instance.commission# 刷单价格


        user.balance =user.balance-price #发布成功 减去用户余额
        print(user,'余额减去',price)
        user.save()

        return instance

    def validate_state(self, state):  # 验证过程



            if state==2:
                raise serializers.ValidationError("不允许把物流订单修改为已完成")
            else:
                return state

    def validate(self,attrs):  # 验证过程

        if attrs["commission"]< 0:
            raise serializers.ValidationError("佣金不能小于0")

        total = attrs['commission']
        balance = attrs['user'].balance
        if balance < total: #余额不能小于订单总价格
            raise serializers.ValidationError("余额不足")
        else:

            return attrs


    class Meta:
        model = LogisticsTask
        # fields = ("id", "user", "money", "Bank_number",'arrival_money','add_time')
        fields = "__all__"




