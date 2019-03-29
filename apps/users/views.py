from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.contrib.auth import get_user_model,authenticate
from .serializers import UserRegSerializer,UserDetailSerializer,UserUpDataSerializer,RechargeSerializer,WithdrawSerializer,StoreSerializer,RechargeSureSerializer,WithdrawSureSerializer
from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import RechargeOrder,WithdrawOrder,Store
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import serializers
User =get_user_model()
# Create your views here.


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(mobile=username))
            print(password)
            a =user.check_password(password)
            print(a)

            # user_is = authenticate(username=username, password=password)
            if user.check_password(password):



                return user
        except Exception as e:

            return None

class GoodstPagination(PageNumberPagination):
    """
    配置分页情况
    """
    page_size = 10
    page_size_query_param = 'page_size'
    # page_query_param = "p"
    max_page_size = 100



class UserViewset(CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):#UpdateModelMixin 修改
    """
    create:
        注册用户
    retrieve:
        用户详情
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()#


    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication )#用户认证方式

    def get_serializer_class(self):#选择序列化方式
        if self.action == "retrieve":
            return UserDetailSerializer#用户详情
        elif self.action == "create":
            return UserRegSerializer#用户注册

        return UserUpDataSerializer

    # permission_classes = (permissions.IsAuthenticated, )
    def get_permissions(self):#动态获取用户权限   注册的时候不需要登入状态    获取详情的时候需要登入状态
        if self.action == "retrieve":#获取详情  user/id
            return [permissions.IsAuthenticated()]
        elif self.action == "create":#注册
            return []

        return []

    def create(self, request, *args, **kwargs):#注册直接登入   重载
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user#返回当前用户

    def perform_create(self, serializer):
        return serializer.save()




class RechargeOrderViewset(CreateModelMixin,viewsets.GenericViewSet):
    """
    充值订单创建与管理
    list:
        获取当前用户充值订单
    create:
        创建充值订单
    """
    permission_classes = (IsAuthenticated)#需要登入
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)#验证方式
    serializer_class = RechargeSerializer#序列化方法
    # pagination_class = GoodstPagination  # 配置分页
    pagination_class = GoodstPagination  # 配置分页

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('user', 'name')





    def get_permissions(self):
        return [permissions.IsAuthenticated()]

    def get_queryset(self):


        return RechargeOrder.objects.filter(user=self.request.user.id).order_by('id')#获取当前用户的订单


    def list(self, request, *args, **kwargs):


        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class RechargeOrderSureViewset(mixins.UpdateModelMixin,viewsets.GenericViewSet):
    """
    充值订单创建与管理
    list:
        管理员查看所有充值订单
    updata:
        管理员确认充值订单
    """
    permission_classes = (IsAuthenticated)#需要登入
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)#验证方式
    serializer_class = RechargeSureSerializer#序列化方法
    # pagination_class = GoodstPagination  # 配置分页
    pagination_class = GoodstPagination  # 配置分页

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('user', 'name')





    def get_permissions(self):
        return [permissions.IsAuthenticated()]

    def get_queryset(self):

        if self.request.user.user_type !=0:
            raise serializers.ValidationError("只有管理员能更改充值订单状态")


        return RechargeOrder.objects.all().order_by('id')#获取当前用户的订单


    def list(self, request, *args, **kwargs):


        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class WithdrawOrderViewset(CreateModelMixin,viewsets.GenericViewSet):
    """
    提现订单管理
    list:
        获取当前用户提现订单
    create:
        创建提现订单
    updata:
        只允许管理员修改订单状态
    """

    permission_classes = (IsAuthenticated)#需要登入
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)#验证方式
    serializer_class = WithdrawSerializer#序列化方法
    # pagination_class = GoodstPagination  # 配置分页
    pagination_class = GoodstPagination  # 配置分页
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


    def get_permissions(self):
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        # print(self.request.user)
        # activity = User.objects.(user=self.request.user.id)

        return WithdrawOrder.objects.filter(user=self.request.user.id).order_by('id')#获取当前用户的订单


    def list(self, request, *args, **kwargs):


        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class WithdrawOrderSureViewset(mixins.UpdateModelMixin,viewsets.GenericViewSet):
    """
    提现订单创建与管理
    list:
        管理员查看所有提现订单
    updata:
        管理员确认 提现充值订单
    """
    permission_classes = (IsAuthenticated)#需要登入
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)#验证方式
    serializer_class = WithdrawSureSerializer#序列化方法
    # pagination_class = GoodstPagination  # 配置分页
    pagination_class = GoodstPagination  # 配置分页

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('user', 'name')





    def get_permissions(self):
        return [permissions.IsAuthenticated()]

    def get_queryset(self):

        if self.request.user.user_type != 0:
            raise serializers.ValidationError("只有管理员能更改提现订单状态")


        return WithdrawOrder.objects.all().order_by('id')#获取所有的订单


    def list(self, request, *args, **kwargs):


        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):



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


class StoreViewset(viewsets.ModelViewSet):
    """
     我的店铺管理
    list:
        获取店铺
    create:
        添加店铺
    update:
        更新店铺
    delete:
        删除店铺
     retrieve:
        用户详情
    """
    pagination_class = GoodstPagination  # 配置分页
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    # authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)#验证方式
    def get_permissions(self):
        return [permissions.IsAuthenticated()]
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)#验证方式
    serializer_class = StoreSerializer#序列化方法

    def get_queryset(self):
        return Store.objects.filter(user=self.request.user.id).order_by('id')#获取当前用户的收货地址

    def list(self, request, *args, **kwargs):
        print(request.data)

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)