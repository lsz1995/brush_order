from django.db import models
from datetime import datetime
# Create your models here.
class Announcement(models.Model):
    """
    用户留言
    """

    title = models.CharField(max_length=100,verbose_name='公告标题')

    content = models.TextField(default="", verbose_name="公告内容", help_text="公告内容")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "公告"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title