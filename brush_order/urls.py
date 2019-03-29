"""china_unicom_crawler_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
import xadmin


from django.views.static import serve

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from brush_order.settings import MEDIA_ROOT
from users.views import UserViewset,RechargeOrderViewset,WithdrawOrderViewset,StoreViewset,RechargeOrderSureViewset,WithdrawOrderSureViewset
from operation.views import AnnouncementViewset

from apps.task.views import BrushTaskViewset,AllBrushTaskViewset,MyTaskViewset,MyTaskOrderViewset,LogisticsTaskViewset
# from task.views import BrushTaskViewset

router = DefaultRouter()
router.register(r'users', UserViewset, base_name="users")
router.register(r'Recharge', RechargeOrderViewset, base_name="Recharge")
router.register(r'RechargeSure', RechargeOrderSureViewset, base_name="RechargeSure")
router.register(r'Withdraw', WithdrawOrderViewset, base_name="Withdraw")
router.register(r'WithdrawSure', WithdrawOrderSureViewset, base_name="WithdrawSure")
router.register(r'store', StoreViewset, base_name="store")
router.register(r'Announcement', AnnouncementViewset, base_name="Announcement")
router.register(r'myactivity', BrushTaskViewset, base_name="myactivity")
router.register(r'allactivity', AllBrushTaskViewset, base_name="allactivity")
router.register(r'order', MyTaskViewset, base_name="order")
router.register(r'MyTask', MyTaskOrderViewset, base_name="MyTask")
router.register(r'LogisticsTask', LogisticsTaskViewset, base_name="LogisticsTask")
# router.register(r'MyLogisticsTask', MyLogisticsTaskViewset, base_name="MyLogisticsTask")
# router.register(r'AllLogisticsTask', AllLogisticsTaskViewset, base_name="AllLogisticsTask")
# router.register(r'LogisticsTaskSure', LogisticsTaskSureViewset, base_name="LogisticsTaskSure")
# router.register(r'SpiderList', SpiderListViewset, base_name="spiderlist")
# router.register(r'data_zfcg', ProcurementListViewset, base_name="zfcg")


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),  # 后台管理
    url(r'^login/', obtain_jwt_token),  # 接收账号密码 生成token签名信息
    url(r'docs/', include_docs_urls(title="接单平台")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': STATIC_ROOT}, name='static')#部署用
#

]
