#coding:utf-8
from django.db import models
from AssetManage.models import Asset
from django.contrib.auth.models import User
from AdvanceManage.models import Scanner,Policies

# Create your models here.
#任务类型
class Type(models.Model):
    name = models.CharField('分类名称',max_length = 50)
    descriptions = models.TextField('分类描述')
    parent = models.ForeignKey('self',verbose_name='上级分类',related_name='type_tasktype',null=True,blank=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        #显示层级菜单
        title_list = [self.name]
        p = self.parent
        while p:
            title_list.insert(0,p.name)
            p = p.parent
        return '-'.join(title_list)
    
    class Meta: 
        verbose_name = 'Type' 
        verbose_name_plural = '任务分类' 
        


class STATUS(models.Model):
    name = models.CharField('任务状态',max_length= 100)
    descriptions = models.TextField('状态描述')
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'STATUS' 
        verbose_name_plural = '任务状态' 


        
class Task(models.Model):
    name = models.CharField('任务名称',max_length=50)
    scan_id = models.CharField('扫描编号',max_length=100,null=True)
    target = models.TextField('扫描目标')
    type = models.ForeignKey(Type,related_name='type_for_task',verbose_name='任务类型',on_delete=models.SET_NULL,null=True)
    targetinfo = models.TextField('任务描述') 
    status = models.ForeignKey(STATUS,verbose_name='任务状态',related_name='status_for_task',default=1,on_delete=models.CASCADE)
    plan_time = models.DateTimeField('计划执行时间',null=True,blank=True)
    
    starttime = models.DateTimeField('开始时间',auto_now_add=True)
    endtime = models.DateTimeField('更新时间',auto_now=True)
    
    scanner = models.ForeignKey(Scanner,related_name='scanner_to_task',on_delete=models.SET_NULL,null=True,verbose_name='扫描器')
    police = models.ForeignKey(Policies,related_name='police_to_task',null=True,on_delete=models.CASCADE,verbose_name='扫描策略')
    
    asset = models.ManyToManyField(Asset,related_name='asset_to_task',verbose_name='资产绑定',limit_choices_to={'type__is_root':False})
    user = models.ForeignKey(User,related_name='task_for_user',null=True,on_delete=models.CASCADE,verbose_name='任务用户')
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Task' 
        verbose_name_plural = '任务管理'
    
    