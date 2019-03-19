from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.
class UserProfile(AbstractUser):#扩展原有user表  setting注册加 AUTH_USER_MODEL='users.UserProfile'
    USER_CHOICES = (
        (0, "管理员"),
        (1, "卖家"),
        (2, "刷手"),
        (3, "代理"),
    )
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female", verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    # my_email = models.EmailField(max_length=110, null=True, blank=True, verbose_name="邮箱")
    qq_number =models.CharField(null=True,blank=True,max_length=15,verbose_name='QQ号码')
    balance =models.FloatField(null=True,verbose_name='余额',default=0)

    user_type = models.IntegerField(default=1, choices=USER_CHOICES, verbose_name="账号类别",
                                      help_text=u"账号类别: 0(管理员),1(卖家),2(刷手),3(代理)")
    Invite_code = models.CharField(default='', blank=True,max_length=8,verbose_name=u'个人邀请码')
    Be_Invite_code = models.CharField(default='', blank=True,max_length=8,verbose_name=u'被邀请码')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
    def get_activity(self):
        return self.brushtask_set.all()

class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name="邀请码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "邀请码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username



class RechargeOrder(models.Model):
    METHOD_CHOICES = (
        (1, "支付宝"),
        (2, "微信"),
        (3, "其他"),
    )
    user =  models.ForeignKey(UserProfile,verbose_name=u'充值用户')
    money = models.FloatField(verbose_name='充值金额')
    arrival_money = models.FloatField(verbose_name='到账金额',default=0)
    order_number = models.CharField(null=True, blank=True, verbose_name="充值单号",max_length=300)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    state = models.BooleanField(default=False,verbose_name='处理状态')
    method = models.IntegerField(default=1, choices=METHOD_CHOICES, verbose_name="充值类别",
                                      help_text=u"充值类别: 1(支付宝),2(微信),3(其他)")
    class Meta:
        verbose_name = "充值订单"
        verbose_name_plural = verbose_name
        # unique_together = ("user",)  # 索引
    def __str__(self):
        return self.order_number


class WithdrawOrder(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'提现用户')
    money = models.FloatField(verbose_name='提现金额')
    Bank_number =models.CharField(null=True, blank=True, verbose_name="提现银行卡号",max_length=50)
    arrival_money = models.FloatField(verbose_name='到账金额',default=0)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    state = models.BooleanField(default=False, verbose_name='处理状态')
    name =models.CharField(default='',max_length=6,verbose_name='银行卡持有人姓名')

    class Meta:
        verbose_name = "提现订单"
        verbose_name_plural = verbose_name
        # unique_together = ("user",)  # 索引
    def __str__(self):
        return self.user.username

class Store(models.Model):
    """
    用户收货地址
    """
    user = models.ForeignKey(UserProfile, verbose_name="用户" )
    store_ww = models.CharField(max_length=100, default="", verbose_name="店铺旺旺")
    store_name = models.CharField(max_length=100, default="", verbose_name="店铺名称")
    store_category = models.CharField(max_length=100, default="", verbose_name="店铺类目")
    store_url = models.URLField(max_length=500,verbose_name='店铺链接')
    sender_name = models.CharField(max_length=100, default="", verbose_name="发件人")
    mobile = models.CharField(max_length=11, default="", verbose_name="电话")
    province = models.CharField(max_length=100, default="", verbose_name="省份")
    city = models.CharField(max_length=100, default="", verbose_name="城市")
    district = models.CharField(max_length=100, default="", verbose_name="区域")
    address = models.CharField(max_length=100, default="", verbose_name="详细地址")
    postal_code = models.CharField(max_length=6, default="", verbose_name="邮编")
    image = models.ImageField(upload_to='store_image', null=True ,blank=True ,default='store_image/default', verbose_name="卖家中心图片")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    state = models.BooleanField(default=False, verbose_name='审核状态')

    class Meta:
        verbose_name = "我的店铺"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.store_name