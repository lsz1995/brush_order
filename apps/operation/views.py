from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.contrib.auth import get_user_model,authenticate
from .serializers import AnnouncementSerializer
from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import Announcement
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


# Create your views here.
class AnnouncementViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取公告列表
    """
    queryset = Announcement.objects.all().order_by("-add_time")
    serializer_class = AnnouncementSerializer