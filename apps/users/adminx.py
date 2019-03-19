# -*- coding:utf-8 -*-
import xadmin

from xadmin import views
from .models import VerifyCode,RechargeOrder,UserProfile,WithdrawOrder,Store
from django.template import loader


class BaseSetting(object):#运行修改主题
    enable_themes=True
    use_bootswatch=True

class GlobalSettings(object):
    site_title = '后台管理系统'#左上角logp
    site_footer = '我的公司'#下方公司
    menu_style = "accordion"#运行菜单收起


class VerifyCodeAdmin(object):
    list_display = ['code','mobile','add_time']  # 后台管理显示地段
    # search_fields = ['Permissions','is_download','note']   # 后台搜索字段
    list_filter = ['code','mobile','add_time']

class RechargeOrderAdmin(object):
    list_display = ['user', 'money', 'order_number','add_time','state','arrival_money','method']  # 后台管理显示地段
    # search_fields = ['user', 'money', 'order_number','add_time','state']   # 后台搜索字段
    list_filter = ['user', 'money', 'order_number','add_time','state','arrival_money','method']


class WithdrawOrderAdmin(object):
    list_display = ['user', 'money', 'Bank_number','arrival_money','name','add_time','state']  # 后台管理显示地段
    # search_fields = ['user', 'money', 'order_number','add_time','state']   # 后台搜索字段
    list_filter = ['user', 'money', 'Bank_number','arrival_money','name','add_time','state']

class StoreAdmin(object):
    list_display = ['user', 'store_ww', 'store_name','store_category','sender_name','mobile','province','city','district','address','postal_code','image','add_time','state']  # 后台管理显示地段
    # search_fields = ['user', 'money', 'order_number','add_time','state']   # 后台搜索字段
    list_filter = ['user', 'store_ww', 'store_name','store_category','sender_name','mobile','province','city','district','address','postal_code','image','add_time','state']


#
# class LinkageUpdateFilter(BaseAdminPlugin):
#     # 默认不加载，只在需要加载的options中设置True来加载
#     is_execute = False
#
#     def init_request(self,*arg,**kwargs):
#         # return self.bool(is_execute)
#
#         return self.is_execute
#
#     def get_media(self, media):
#         # 此处用来加入我们自己的js文件
#         print('触发')
#         # media = media + self.vendor("xadmin.self.update_select.js")
#         return media




# xadmin.site.register_plugin(HelloWorldPlugin, UpdateAdminView)
# xadmin.site.register(VerifyCode,VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)#注册主题
xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.register(RechargeOrder,RechargeOrderAdmin)
xadmin.site.register(WithdrawOrder,WithdrawOrderAdmin)
xadmin.site.register(Store,StoreAdmin)
# -*- coding:utf-8 -*-