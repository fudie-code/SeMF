#coding:utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Log(models.Model):
    type = models.CharField(u'操作类型',max_length=50)
    user = models.ForeignKey(User,verbose_name=u'人员关联',related_name='log_user',on_delete=models.CASCADE,)
    action = models.TextField(u'用户操作')
    status = models.NullBooleanField('操作状态',default=True)
    create_time = models.DateTimeField('操作时间',auto_now_add=True)
    
    def __str__(self):
        return self.type