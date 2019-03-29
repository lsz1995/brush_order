# -*- coding:utf-8 -*-
import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import datetime
from datetime import timedelta
from rest_framework.validators import UniqueValidator
from .models import VerifyCode
from django.db.models import Q
from .models import RechargeOrder,WithdrawOrder,Store
User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):##获取详情
    """
    用户详情序列化类
    """
    user = serializers.HiddenField(#
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = User
        fields = ("id",'user',"username", "qq_number", "email", "mobile",'balance','user_type','date_joined')




class UserUpDataSerializer(serializers.ModelSerializer):#修改密码
    """
    用户修改密码序列化类
    """
    user = serializers.HiddenField(#
        default=serializers.CurrentUserDefault()
    )
    password = serializers.CharField(
        style={'input_type': 'password'},help_text="密码", label="密码",write_only=True,  #style  设置密码密文  write_only  序列化就不会带上password
    )
    old_password = serializers.CharField(
        style={'input_type': 'password'},help_text="旧密码", label="旧密码",write_only=True,  #style  设置密码密文  write_only  序列化就不会带上password
    )

    def validate_old_password(self, old_password):#验证过程

        a = self.instance.check_password(old_password)

        if a:
            pass
        else:

            raise serializers.ValidationError("旧密码错误")





    def update(self, instance, validated_data):#更新过程


        # Simply set each attribute on the instance, and then save it.
        # Note that unlike `.create()` we don't need to treat many-to-many
        # relationships as being a special case. During updates we already
        # have an instance pk for the relationships to be associated with.
        password = validated_data['password']
        instance.set_password(password)
        instance.save()

        return instance



    class Meta:
        model = User
        fields = ('user',"id",'password','old_password')







# class UserRegSerializer(serializers.ModelSerializer):#    ModelSerializer    注册
#     #验证码改邀请码
#
#     code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4,label="邀请码",#  write_only  序列化就不会带上code
#                                  error_messages={
#                                      "blank": "请输入邀请码",
#                                      "required": "请输入邀请码",
#                                      "max_length": "邀请码格式错误",
#                                      "min_length": "邀请码格式错误"
#                                  },
#                                  help_text="邀请码")
#     username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
#                                      validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])
#
#     password = serializers.CharField(
#         style={'input_type': 'password'},help_text="密码", label="密码", write_only=True,#style  设置密码密文  write_only  序列化就不会带上password
#     )
#
#     #上面是对POST过来的数据进行验证 ， 并进行验证
#
#     # def create(self, validated_data):
#     #     user = super(UserRegSerializer, self).create(validated_data=validated_data)# 创建用户
#     #     user.set_password(validated_data["password"])
#     #     user.save()
#     #     return user
#
#     def validate_code(self, code):#验证验证码
#         # try:
#         #     verify_records = VerifyCode.objects.get(mobile=self.initial_data["username"], code=code)
#         # except VerifyCode.DoesNotExist as e:
#         #     pass
#         # except VerifyCode.MultipleObjectsReturned as e:
#         #     pass
#
#         print(self.initial_data["username"])
#         print(self.initial_data["code"])
#         verify_records = VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by("-add_time")
#         if verify_records:
#             last_record = verify_records[0]
#             if last_record.code != code:
#                 raise serializers.ValidationError("邀请码错误")
#         else:
#             raise serializers.ValidationError("邀请码错误")
#         print('sssss')#之后改成创建钱包表
#         # if verify_records:#有时间限制
#         #     last_record = verify_records[0]
#         #
#         #     five_mintes_ago = datetime.now() - timedelta(hours=1, minutes=0, seconds=0)
#         #     if five_mintes_ago > last_record.add_time:
#         #         raise serializers.ValidationError("验证码过期")
#         #
#         #     if last_record.code != code:
#         #         raise serializers.ValidationError("验证码错误")
#         #
#         # else:
#         #     raise serializers.ValidationError("验证码错误")
#
#     def validate(self, attrs):#作用于所有的serializers
#         attrs["mobile"] = attrs["username"]
#         del attrs["code"]
#         return attrs
#
#     class Meta:
#         model = User
#         # fields = ("username", "code",'mobile',"password")
#         fields = ("username", "mobile","password")


class UserRegSerializer(serializers.ModelSerializer):#    ModelSerializer    注册
    password = serializers.CharField(
        style={'input_type': 'password'},help_text="密码", label="密码",write_only=True,  #style  设置密码密文  write_only  序列化就不会带上password
    )

    def create(self, validated_data):
        user = super(UserRegSerializer, self).create(validated_data=validated_data)# 创建用户
        user.set_password(validated_data["password"])
        user.save()
        return user


    # def validate_mobile(self, mobile):#验证过程
    #
    #
    #     mobile_records = User.objects.filter(mobile=mobile)
    #     if mobile_records:
    #
    #         raise serializers.ValidationError("电话号码已存在")

    def validate(self, attrs):  # 验证充值金额

        mobile_records = User.objects.filter(mobile=attrs['mobile'])
        if mobile_records:

            raise serializers.ValidationError("电话号码已存在")

        # user_records = User.objects.filter(username=attrs['username'])
        #
        # if user_records:
        #
        #     raise serializers.ValidationError("用户已存在")

        return attrs


    class Meta:
        model = User
        # fields = ("username", "code",'mobile',"password")
        fields = ("username", "mobile","password",'email','qq_number','Be_Invite_code','user_type')


class RechargeSerializer(serializers.ModelSerializer):
    #创建充值订单，查看充值订单
    user = serializers.HiddenField(#
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')



    def validate(self,attrs):  # 验证充值金额

        if attrs['arrival_money']<= 0 or attrs['money']<= 0 :
            raise serializers.ValidationError("充值金额不能小于等于0")
        if attrs['state']==True:
            raise serializers.ValidationError("提现订单初始状态必须为待处理")
        return attrs

    class Meta:
        model = RechargeOrder
        fields = ("id", "user", "money",'method', "order_number",'arrival_money','add_time','state')

class RechargeSureSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(  #
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    def validate_state(self, state):  # 验证充值金额
        if state ==False:
            raise serializers.ValidationError("状态未改变")



    def update(self, instance, validated_data):  #确认订单后给 充值用户加钱


        if instance.state ==True:
            raise serializers.ValidationError("无法操作已处理完订单")

        instance.user.balance += instance.arrival_money
        instance.state = True
        instance.user.save()
        instance.save()

        print(instance.user)
        print('到账')
        print(instance.arrival_money)

        return  instance



    class Meta:
        model = RechargeOrder
        fields = ("id", "user", "money", 'method', "order_number", 'arrival_money', 'add_time', 'state')






class WithdrawSerializer(serializers.ModelSerializer):
    #创建提现订单，查看提现订单
    user = serializers.HiddenField(#
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    def create(self, validated_data):

        user = validated_data['user']
        user.balance =user.balance -validated_data['money']#提现 扣除提现订单用户余额
        user.save()
        print(user,'扣除',validated_data['money'])


        instance = WithdrawOrder.objects.create(**validated_data)
        instance.save()
        return instance




    def validate(self,attrs):  # 验证过程订单金额不能小于0


        if attrs['user'].balance < attrs['money']:
                raise serializers.ValidationError("余额不足")

        if attrs['arrival_money']<= 0 or attrs['money']<= 0 :
                raise serializers.ValidationError("提现金额不能小于等于0")
        if attrs['state'] !=False:
            raise serializers.ValidationError("提现订单初始状态必须为待处理")
        return attrs



    class Meta:
        model = WithdrawOrder
        fields = ("id", "user", "money", "Bank_number",'name','arrival_money','add_time','state')


class WithdrawSureSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(  #
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    def validate_state(self, state):  # 验证修改提现订单状态


        if state ==False:
            raise serializers.ValidationError("状态未改变")
        return state





    class Meta:
        model = WithdrawOrder
        fields = ("id", "user", "money", "Bank_number",'name','arrival_money','add_time','state')





class StoreSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(#
        default=serializers.CurrentUserDefault()
    )


    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    # state =serializers.BooleanField(read_only=True)
    def validate(self,attrs):  # 验证过程订单金额不能小于0
        if attrs['state'] ==True:
            raise serializers.ValidationError("必须由管理员审核")

        return attrs




    class Meta:
        model = Store
        # fields = ('id','user', 'store_ww', 'store_name','store_category','store_url','sender_name','mobile','province','city','district','address','postal_code','image','add_time',)
        fields = "__all__"