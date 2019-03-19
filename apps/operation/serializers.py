# -*- coding:utf-8 -*-
import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import datetime
from datetime import timedelta
from rest_framework.validators import UniqueValidator

from django.db.models import Q
from .models import Announcement
User = get_user_model()


class AnnouncementSerializer(serializers.ModelSerializer):##获取详情
    """
    公告序列化
    """


    class Meta:
        model = Announcement
        fields = ("id","title", "content", "add_time")
