from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.contrib.auth import get_user_model,authenticate
from .serializers import BrushTaskSerializer,AllBrushTask,OrderInfosSerializer,GetOrderInfosSerializer,LogisticsTaskSerializer
from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import BrushTask,OrderInfos,LogisticsTask,LogisticsTaskOrder
# from apps.users.models import UserProfile
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import serializers
User=get_user_model()
# Create your views here.

class GoodstPagination(PageNumberPagination):
    """
    配置分页情况
    """
    page_size = 10
    page_size_query_param = 'page_size'
    # page_query_param = "p"
    max_page_size = 100

class BrushTaskViewset(CreateModelMixin,viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,):
    """
    我的活动管理
    list:
        获取当前用户活动列表与详情
    create:
        用当前登入账号创建活动
    update:
        更新物流订单
     retrieve:
        物流订单详情
    """

    permission_classes = (IsAuthenticated)#需要登入
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)#验证方式
    serializer_class = BrushTaskSerializer#序列化方法
    # pagination_class = GoodstPagination  # 配置分页
    pagination_class = GoodstPagination  # 配置分页

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # search_fields = ('name', 'desc',)



    def get_permissions(self):
        return [permissions.IsAuthenticated()]

    def get_queryset(self):

        print(self.request.POST)
        return BrushTask.objects.filter(user=self.request.user.id)#获取当前用户的订单

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        if not instance.state:
            raise serializers.ValidationError("已关闭活动，无法修改操作")

        for key,value in request.data.items():
            if key =='single_price':
                raise serializers.ValidationError("本金不能修改")
            elif key =='commission' :
                raise serializers.ValidationError("佣金不能修改")
            elif key =='numbers' :
                raise serializers.ValidationError("单数不能修改")
            elif key=='state':
                if not value:
                    back_price =(instance.commission+instance.single_price)*instance.numbers

                    instance.user.balance-= instance.user.balance -back_price
                    instance.user.save()
                    print(instance.user,'余额加上',back_price)
                    print('想要关闭活动')









        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


    def list(self, request, *args, **kwargs):


        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class AllBrushTaskViewset(mixins.ListModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        获取所有活动
     retrieve:
        根据ID获取活动详情
    """
    # 取数据
    # queryset = CourseOrg.objects.all()



    queryset = BrushTask.objects.all()#获取数据库所有内容
    serializer_class = AllBrushTask#序列化数据
    pagination_class = GoodstPagination#配置分页
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'desc',)


    # @detail_route(renderer_classes=[StaticHTMLRenderer])
    # def start(self, request, *args, **kwargs):
    #     print('爬虫开始')
    #     print(self.request.user)
    #
    #     return Response(self.request.user)

    def list(self, request, *args, **kwargs):


        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class MyTaskViewset(CreateModelMixin,viewsets.GenericViewSet,mixins.UpdateModelMixin, mixins.RetrieveModelMixin,):
    """
    接受任务和查看已接任务
    list:
        获取当前已接任务
    create:
        接受任务
    updata:
        提交订单信息，可修改为审核中状态，该接口无法将订单状态改为完成
    """

    permission_classes = (IsAuthenticated)#需要登入
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)#验证方式
    serializer_class = OrderInfosSerializer#序列化方法
    # pagination_class = GoodstPagination  # 配置分页
    pagination_class = GoodstPagination  # 配置分页
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # def get_serializer_class(self):#选择序列化方式
    #     if self.action == "updata":
    #         return UserDetailSerializer#用户详情
    #     elif self.action == "create":
    #         return UserRegSerializer#用户注册
    #
    #     return UserUpDataSerializer



    def get_permissions(self):
        return [permissions.IsAuthenticated()]

    def get_queryset(self):


        return OrderInfos.objects.filter(user=self.request.user.id)#获取当前用户的订单


    def list(self, request, *args, **kwargs):


        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):

        for key,value in request.data.items():
            if key =='single_price':
                raise serializers.ValidationError("本金不能修改")
            elif key =='commission' :
                raise serializers.ValidationError("佣金不能修改")
            elif key=='activity':
                raise serializers.ValidationError("不能修改订单所属活动")

        try:
            is_true =request.data['state_type']
        except:
            raise serializers.ValidationError("缺少状态参数")
        if int(is_true) != 3:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        else:
            raise serializers.ValidationError("没有权限确认")

class MyTaskOrderViewset(viewsets.GenericViewSet,mixins.UpdateModelMixin, mixins.RetrieveModelMixin):

    """
    获取卖家发布所有活动的所有已被接的任务订单updata:只能改变订单状态
    list:
        获取当前卖家发布所有活动的所有已被接的任务订单
    updata:
        卖家确认订单完成（只能操作本人发布活动所属订单）

    """

    permission_classes = (IsAuthenticated)#需要登入
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)#验证方式
    serializer_class = GetOrderInfosSerializer#序列化方法
    # pagination_class = GoodstPagination  # 配置分页
    pagination_class = GoodstPagination  # 配置分页
    queryset = OrderInfos.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # queryset = OrderInfos


    def get_permissions(self):
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        if self.action == "list":
            order = []
            activity =BrushTask.objects.filter(user_id=self.request.user.id)
            # activity1 =self.request.user.brushtask_set.all()
            for act in activity:
                ord = OrderInfos.objects.filter(activity_id= act.id)
                for i in ord:
                    order.append(i)

            # print('总共',len(order))
            return order#获取当前用户的订单
        else:
            return OrderInfos.objects.all().order_by('id')



    def update(self, request, *args, **kwargs):





        partial = kwargs.pop('partial', False)
        instance = self.get_object()


        if request.user ==instance.activity.user:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        else:
            # return Response(serializers.ValidationError("不是活动创建者订单无法确认"))
            raise serializers.ValidationError("不是活动创建者，无法确认")



    def list(self, request, *args, **kwargs):


        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# class LogisticsTaskViewset(CreateModelMixin,viewsets.GenericViewSet):
#
#     """
#     卖家的物流活动管理
#     list:
#         获取当前卖家的物流活动列表与详情
#     create:
#         用当前登入账号创建物流活动
#     """
#
#     permission_classes = (IsAuthenticated)#需要登入
#     authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)#验证方式
#     serializer_class = LogisticsTaskSerializer#序列化方法
#     # pagination_class = GoodstPagination  # 配置分页
#     pagination_class = GoodstPagination  # 配置分页
#
#     filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
#     # search_fields = ('name', 'desc',)
#
#
#
#     def get_permissions(self):
#         return [permissions.IsAuthenticated()]
#
#     def get_queryset(self):
#
#         print(len(LogisticsTask.objects.filter(user=self.request.user.id)))
#         return LogisticsTask.objects.filter(user=self.request.user.id)#获取当前用户的订单
#
#
#     def list(self, request, *args, **kwargs):
#
#
#         queryset = self.filter_queryset(self.get_queryset())
#
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#
#             return self.get_paginated_response(serializer.data)
#
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#
# class MyLogisticsTaskViewset(CreateModelMixin,viewsets.GenericViewSet,mixins.UpdateModelMixin, mixins.RetrieveModelMixin,):
#     """
#     刷手所接物流任务
#     list:
#         获取刷手当前已接任务
#     create:
#         接受物流任务
#     updata:
#         提交物流订单信息，可修改为审核中状态，该接口无法将订单状态改为完成
#     """
#
#     permission_classes = (IsAuthenticated)#需要登入
#     authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)#验证方式
#     serializer_class = MyLogisticsTaskInfoSerializer#序列化方法
#     # pagination_class = GoodstPagination  # 配置分页
#     pagination_class = GoodstPagination  # 配置分页
#     filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
#     # def get_serializer_class(self):#选择序列化方式
#     #     if self.action == "updata":
#     #         return UserDetailSerializer#用户详情
#     #     elif self.action == "create":
#     #         return UserRegSerializer#用户注册
#     #
#     #     return UserUpDataSerializer
#
#
#
#     def get_permissions(self):
#         return [permissions.IsAuthenticated()]
#
#     def get_queryset(self):
#
#
#         return LogisticsTaskOrder.objects.filter(user=self.request.user.id)#获取当前用户的订单
#
#
#     def list(self, request, *args, **kwargs):
#
#
#         queryset = self.filter_queryset(self.get_queryset())
#
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#
#     # def update(self, request, *args, **kwargs):
#     #     is_true =request.data['state_type']
#     #
#     #     if int(is_true) != 3:
#     #         partial = kwargs.pop('partial', False)
#     #         instance = self.get_object()
#     #         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#     #         serializer.is_valid(raise_exception=True)
#     #         self.perform_update(serializer)
#     #
#     #         if getattr(instance, '_prefetched_objects_cache', None):
#     #             # If 'prefetch_related' has been applied to a queryset, we need to
#     #             # forcibly invalidate the prefetch cache on the instance.
#     #             instance._prefetched_objects_cache = {}
#     #
#     #         return Response(serializer.data)
#     #     else:
#     #         raise serializers.ValidationError("没有权限确认")
#
# class AllLogisticsTaskViewset(mixins.ListModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     """
#     list:
#         获取所有活动
#      retrieve:
#         根据ID获取活动详情
#     """
#     # 取数据
#     # queryset = CourseOrg.objects.all()
#
#
#
#     queryset = LogisticsTask.objects.all()#获取数据库所有内容
#     serializer_class = AllLogisticsTask#序列化数据
#     pagination_class = GoodstPagination#配置分页
#     filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
#     search_fields = ('name', 'desc',)
#
#
#     # @detail_route(renderer_classes=[StaticHTMLRenderer])
#     # def start(self, request, *args, **kwargs):
#     #     print('爬虫开始')
#     #     print(self.request.user)
#     #
#     #     return Response(self.request.user)
#
#     def list(self, request, *args, **kwargs):
#
#
#         queryset = self.filter_queryset(self.get_queryset())
#
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#
#
# class LogisticsTaskSureViewset(viewsets.GenericViewSet,mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
#
#     """
#     获取卖家发布所有活动的所有已被接的任务订单updata:只能改变订单状态
#     list:
#         获取当前卖家发布所有活动的所有已被接的任务订单
#     updata:
#         卖家确认订单完成（只能操作本人发布活动所属订单且只能更改订单状态）
#     read:
#         查看某笔物流订单
#
#
#     """
#
#     permission_classes = (IsAuthenticated)#需要登入
#     authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)#验证方式
#     serializer_class = LogisticsTaskSureSerializer#序列化方法
#     # pagination_class = GoodstPagination  # 配置分页
#     pagination_class = GoodstPagination  # 配置分页
#     queryset = LogisticsTaskOrder.objects.all()
#     filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
#     # queryset = OrderInfos
#
#
#     def get_permissions(self):
#         return [permissions.IsAuthenticated()]
#
#     def get_queryset(self):
#         if self.action == "list":
#             order = []
#             # task =LogisticsTask.objects.filter(user_id=self.request.user.id)
#             task =self.request.user.logisticstask_set.all()
#             # activity1 =self.request.user.brushtask_set.all()
#             for act in task:
#                 ord = LogisticsTaskOrder.objects.filter(task_id=act.id)
#                 for i in ord:
#                     order.append(i)
#
#             # print('总共',len(order))
#             return order#获取当前用户所发布的所有物流任务的订单
#         else:
#             return LogisticsTaskOrder.objects.all()
#
#
#
#     def update(self, request, *args, **kwargs):
#
#
#
#
#
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#
#
#         if request.user ==instance.task.user:
#             serializer = self.get_serializer(instance, data=request.data, partial=partial)
#             serializer.is_valid(raise_exception=True)
#             self.perform_update(serializer)
#
#             if getattr(instance, '_prefetched_objects_cache', None):
#                 # If 'prefetch_related' has been applied to a queryset, we need to
#                 # forcibly invalidate the prefetch cache on the instance.
#                 instance._prefetched_objects_cache = {}
#
#             return Response(serializer.data)
#         else:
#             # return Response(serializers.ValidationError("不是活动创建者订单无法确认"))
#             raise serializers.ValidationError("当前登入用户不是物流活动创建者，无法确认")
#
#
#
#     def list(self, request, *args, **kwargs):
#
#
#         queryset = self.filter_queryset(self.get_queryset())
#
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)



class LogisticsTaskViewset(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    """
     我的物流订单管理
    list:
        获取我的物流订单
    create:
        添加物流订单
    update:
        更新物流订单
     retrieve:
        物流订单详情
    """

    permission_classes = (IsAuthenticated)#需要登入
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)#验证方式
    serializer_class = LogisticsTaskSerializer#序列化方法
    # pagination_class = GoodstPagination  # 配置分页
    pagination_class = GoodstPagination  # 配置分页

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # search_fields = ('name', 'desc',)



    def get_permissions(self):
        return [permissions.IsAuthenticated()]

    def get_queryset(self):

        print(len(LogisticsTask.objects.filter(user=self.request.user.id)))
        return LogisticsTask.objects.filter(user=self.request.user.id).order_by('id')#获取当前用户的订单


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance.state ==1:
            raise serializers.ValidationError("已取消订单，无法操作")

        try:
            cancel = request.data['state']

        except:
            cancel = 0
        if int(cancel) ==1:

            request.user.balance = request.user.balance -instance.commission
            request.user.save()
            print(request.user,'余额加',instance.commission)


        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def list(self, request, *args, **kwargs):


        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)