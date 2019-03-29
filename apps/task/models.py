from django.db import models
from datetime import datetime
from users.models import UserProfile
# Create your models here.


class LogisticsTask(models.Model):
    """
    物流任务
    """
    LogisticsTask_CHOICES = (
        (0, "等待完成"),
        (1, "已取消"),
        (2, "已完成"),
    )
    user = models.ForeignKey(UserProfile,verbose_name='任务发布者',help_text='任务发布者')

    receive_name = models.CharField(max_length=100, default="", verbose_name="收货人",help_text='收货人')
    mobile = models.CharField(max_length=11, default="", verbose_name="收货人电话",help_text='收货人电话')
    province = models.CharField(max_length=100, default="", verbose_name="省份",help_text='省份')
    city = models.CharField(max_length=100, default="", verbose_name="城市",help_text='城市')
    district = models.CharField(max_length=100, default="", verbose_name="区域",help_text='区域')
    address = models.CharField(max_length=100, default="", verbose_name="详细地址",help_text='详细地址')
    postal_code = models.CharField(max_length=6, default="", verbose_name="邮编",help_text='邮编')
    # state = models.BooleanField(default=False,verbose_name='任务完成状态',help_text='任务完成状态')
    state = models.IntegerField(default=0, choices=LogisticsTask_CHOICES, verbose_name="任务状态",
                                      help_text=u"任务状态: 0(等待完成),1(已取消),2(已完成)")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间",help_text='添加时间')
    commission = models.FloatField(default=0,verbose_name=u'佣金',help_text='佣金')

    Courier_number = models.CharField(max_length=100,default='',blank=True, verbose_name=u'快递单号',help_text='快递单号')
    content = models.TextField(default="", blank=True,verbose_name="物流信息", help_text="物流信息")
    class Meta:
        verbose_name = "物流任务"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.receive_name

class LogisticsTaskOrder(models.Model):

    task = models.ForeignKey(LogisticsTask,verbose_name=u'所接物流任务',help_text='所接物流任务')
    user  = models.ForeignKey(UserProfile,verbose_name='接受任务者',help_text='接受任务者')
    commission = models.FloatField(default=0,verbose_name=u'佣金',help_text='佣金')
    receive_name = models.CharField(max_length=100, default="", verbose_name="收货人",help_text='收货人')
    mobile = models.CharField(max_length=11, default="", verbose_name="收货人电话",help_text='收货人电话')
    state = models.BooleanField(default=False, verbose_name='任务状态',help_text='任务状态')
    # state = models.IntegerField(default=1, choices=BUY_CHOICES, verbose_name="任务状态",
    #                                   help_text=u"任务状态: 1(等待完成),2(已取消),3(已完成)")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间",help_text='添加时间')
    Courier_number = models.CharField(max_length=100,default='',blank=True, verbose_name=u'快递单号',help_text='快递单号')
    content = models.TextField(default="", blank=True,verbose_name="物流信息", help_text="物流信息")
    class Meta:
        verbose_name = "物流任务订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.task.receive_name

class BrushTask(models.Model):
    BUY_CHOICES = (
        (1, "不限"),
        (2, "男"),
        (3, "女"),
    )

    user = models.ForeignKey(UserProfile, verbose_name=u'刷单任务发布者',help_text='刷单任务发布者')
    product_url = models.CharField(max_length=500,verbose_name=u'产品链接',help_text='产品链接')
    store_ww =models.CharField(max_length=50,verbose_name=u'店铺旺旺',help_text='店铺旺旺')
    store_name = models.CharField(max_length=50, verbose_name=u'店铺名称',help_text='店铺名称')
    single_price = models.FloatField(default=0,max_length=600,verbose_name=u'本金',help_text='本金')
    commission = models.FloatField(default=0,verbose_name=u'佣金',help_text='佣金')

    numbers = models.IntegerField(default=0,verbose_name=u'剩余刷单次数',help_text='剩余刷单次数')

    is_consulting_service = models.BooleanField(default=False,verbose_name='是否咨询客服',help_text='是否咨询客服')
    activity_sku =models.CharField(max_length=100,verbose_name='活动SKU选项',help_text='活动SKU选项')
    order_message = models.CharField(max_length=100, verbose_name='网店订单留言',help_text='网店订单留言')
    added_message = models.CharField(max_length=500, verbose_name='补充说明',help_text='补充说明')
    title = models.CharField(max_length=300, verbose_name='活动标题',help_text='活动标题')
    client_type = models.CharField(max_length=50,verbose_name='客户端类型',help_text='客户端类型')
    image = models.ImageField(upload_to='activity_image', blank=True,verbose_name="活动图片",help_text='活动图片')
    activity_platform = models.CharField(max_length=100,verbose_name='活动平台',help_text='活动平台')
    activity_entrance = models.CharField(max_length=100,verbose_name='活动入口',help_text='活动入口')
    activity_keyword = models.CharField(max_length=100,verbose_name='进店关键字',help_text='进店关键字')
    search_rank = models.CharField(max_length=100, verbose_name='搜索排序',help_text='搜索排序')
    price_highest = models.FloatField(verbose_name='最高价格',help_text='最高价格')
    price_minimum = models.FloatField(verbose_name='最低价格',help_text='最低价格')
    delivery_place = models.CharField(max_length=100, verbose_name='发货地',help_text='发货地')
    style= models.CharField(max_length=100, verbose_name='款式',help_text='款式')
    before_activity = models.CharField(max_length=100,verbose_name=u'活动前',help_text='活动前')
    order_payment_time = models.CharField(max_length=100,verbose_name=u'下单付款时间',help_text='下单付款时间')
    allow_pay = models.CharField(max_length=200,verbose_name=u'允许付款方式（用逗号隔开）',help_text='允许付款方式（用逗号隔开）')
    evaluation =models.CharField(max_length=200,verbose_name=u'产品自评',help_text='产品自评')
    is_photo =models.BooleanField(default=False,verbose_name='是否实拍',help_text='是否实拍')
    message_type = models.IntegerField(default=1, choices=BUY_CHOICES, verbose_name="买家性别",
                                      help_text=u"买家性别: 1(不限),2(男),3(女)")
    activity_interval = models.CharField(max_length=200,verbose_name='活动间隔',help_text='活动间隔')
    state = models.BooleanField(default=True, verbose_name='活动状态',help_text='活动状态')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间",help_text='添加时间')


    class Meta:
        verbose_name = "刷单活动"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_activity_order(self):
        return self.orderinfos_set.all()#教师的外键是机构      机构中可取教师数量

    


class OrderInfos(models.Model):
    STATE_CHOICES = (
        (1, "已接单"),
        (2, "审核中"),
        (3, "已确认"),
    )

    user = models.ForeignKey(UserProfile,verbose_name='接单人',help_text='接单人')

    activity = models.ForeignKey(BrushTask,verbose_name=u'所接任务',help_text='所接任务')

    activity_name =models.CharField(default='',max_length=500,verbose_name=u'活动名称',help_text='活动名称')
    single_price = models.FloatField(default=0,verbose_name=u'本金',help_text='本金（商品价格）')

    commission = models.FloatField(default=0,verbose_name=u'佣金',help_text='佣金（平台共收多少钱）')

    add_time = models.DateTimeField(default=datetime.now, verbose_name="接单时间",help_text='接单时间')


    state_type = models.IntegerField(default=1, choices=STATE_CHOICES, verbose_name="订单状态",
                                      help_text=u"订单状态: 1(已接单),2(审核中),3(已确认)")

    buyer = models.CharField(max_length=100,default='',blank=True,verbose_name=u'买家',help_text='买家')
    order = models.CharField(max_length=100,default='',blank=True,verbose_name=u'订单号',help_text='订单号')
    Courier = models.CharField(max_length=100,default='',blank=True, verbose_name=u'快递',help_text='什么快递')
    Courier_number = models.CharField(max_length=100,default='',blank=True, verbose_name=u'快递单号',help_text='快递单号')

    class Meta:
        verbose_name = "接单订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.activity.title
