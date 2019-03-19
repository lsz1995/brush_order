# -*- coding:utf-8 -*-
import xadmin


from .models import Announcement
from django.template import loader




class AnnouncementAdmin(object):
    list_display = ['title','content','add_time']  # 后台管理显示地段
    # search_fields = ['Permissions','is_download','note']   # 后台搜索字段
    list_filter =  ['title','content','add_time']

xadmin.site.register(Announcement,AnnouncementAdmin)