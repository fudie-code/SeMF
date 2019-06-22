#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone


# Create your models here.
class Notice(models.Model):
    title = models.CharField(verbose_name=u'通知标题', max_length=200)
    body = models.TextField(verbose_name=u'通知内容', null=True, blank=True)
    is_read = models.BooleanField(verbose_name = '是否阅读',default=False)
    user = models.ForeignKey(User,related_name='notice_user',
                             verbose_name=u'创建用户', on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(verbose_name=u'通知时间', default=timezone.now)

    def __str__(self):
        return self.title
    
    class Meta: 
        verbose_name = 'Notice' 
        verbose_name_plural = '通告管理'