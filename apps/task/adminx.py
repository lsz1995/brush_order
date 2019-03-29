# -*- coding:utf-8 -*-
import xadmin


from .models import BrushTask,OrderInfos,LogisticsTask,LogisticsTaskOrder
from django.template import loader



class AnnouncementAdmin(object):
    list_display = ['user','store_name','single_price','numbers','title','add_time']  # 后台管理显示地段
    # search_fields = ['Permissions','is_download','note']   # 后台搜索字段
    list_filter =  ['user','store_name','single_price','numbers','title','add_time']

class OrderInfosAdmin(object):
    list_display = ['user','activity','single_price','commission','add_time','state_type','buyer','order','Courier','Courier_number']  # 后台管理显示地段
    # search_fields = ['Permissions','is_download','note']   # 后台搜索字段
    list_filter =  ['user','activity','single_price','commission','add_time','state_type','buyer','order','Courier','Courier_number']

class LogisticsTaskAdmin(object):
    list_display = ['user','receive_name','mobile','province','city','district','address','postal_code','state','add_time','Courier_number','content']  # 后台管理显示地段
    # search_fields = ['Permissions','is_download','note']   # 后台搜索字段
    list_filter =  ['user','receive_name','mobile','province','city','district','address','postal_code','state','add_time','Courier_number','content']

class LogisticsTaskOrderAdmin(object):
    list_display = ['task','user','state','Courier_number','content','add_time']  # 后台管理显示地段
    # search_fields = ['Permissions','is_download','note']   # 后台搜索字段
    list_filter =  ['task','user','state','Courier_number','content','add_time']


xadmin.site.register(BrushTask,AnnouncementAdmin)
xadmin.site.register(OrderInfos,OrderInfosAdmin)

xadmin.site.register(LogisticsTask,LogisticsTaskAdmin)
# xadmin.site.register(LogisticsTaskOrder,LogisticsTaskOrderAdmin)

