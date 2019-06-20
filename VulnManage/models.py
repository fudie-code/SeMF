#coding:utf-8

from django.db import models
from AssetManage.models import Asset
# Create your models here.
class LEVEL(models.Model):
    name = models.CharField('风险等级',max_length= 100)
    descriptions = models.TextField('分类描述')
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'LEVEL' 
        verbose_name_plural = '风险等级' 

class STATUS(models.Model):
    name = models.CharField('漏洞状态',max_length= 100)
    descriptions = models.TextField('分类描述')
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'STATUS' 
        verbose_name_plural = '漏洞状态' 

class Type(models.Model):
    name = models.CharField('分类名称',max_length = 50)
    descriptions = models.TextField('分类描述')
    parent = models.ForeignKey('self',verbose_name='上级分类',related_name='type_vuln',null=True,blank=True,on_delete=models.SET_NULL)
    
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
        verbose_name_plural = '漏洞分类' 
        

#用来记录各种来源与资产相关的漏洞
class Vuln(models.Model):
    name = models.CharField('漏洞名称',max_length = 50)
    cve = models.CharField('CVE',max_length = 50,null=True,blank=True)
    type = models.ForeignKey(Type,verbose_name='漏洞分类',related_name='type_for_vuln',null=True,blank=True,on_delete=models.SET_NULL)
    level = models.ForeignKey(LEVEL,verbose_name='漏洞分级',related_name='level_for_vuln',null=True,blank=True,on_delete=models.SET_NULL)
    introduce = models.TextField('漏洞简介',null=True)
    info = models.TextField('漏洞信息',null=True)
    scopen = models.TextField('影响范围')
    fix = models.TextField('修复方案',null=True)
    fix_status = models.ForeignKey(STATUS,verbose_name='修复状态',related_name='status_for_vuln',null=True,on_delete=models.SET_NULL)
    action = models.TextField('修复记录',null=True)
    create_data = models.DateTimeField('发现时间',auto_now_add=True)
    update_data = models.DateTimeField('更新时间',auto_now=True)
    
    #task = models.ForeignKey(Task,related_name='vuln_for_task',on_delete=models.SET_NULL,null=True,blank=True)
    asset = models.ForeignKey(Asset,related_name='vuln_for_asset',on_delete=models.CASCADE,limit_choices_to={'type__is_root':False})
    
    def __str__(self):
        return self.name 
    
    class Meta: 
        verbose_name = 'Vuln' 
        verbose_name_plural = '资产漏洞' 
        
        
        
#漏洞来源，主要用来自定义漏洞来源，实现后续的动态扩展
class Source(models.Model):
    name = models.CharField('漏洞来源',max_length = 50)
    descriptions = models.TextField('来源描述')
    parent = models.ForeignKey('self',verbose_name='上级分类',related_name='source_vuln',null=True,blank=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        #显示层级菜单
        title_list = [self.name]
        p = self.parent
        while p:
            title_list.insert(0,p.name)
            p = p.parent
        return '-'.join(title_list)
    
    class Meta: 
        verbose_name = 'Source' 
        verbose_name_plural = '漏洞来源' 


#用来修正自动化扫描工具带来的误报，或者漏洞描述、修复方案的补充
class AdvanceVuln(models.Model):
    source = models.ForeignKey(Source,verbose_name='漏洞来源',related_name='source_for_advancevuln',null=True,blank=True,on_delete=models.SET_NULL)
    vuln_name=models.CharField('漏洞名称',max_length=255)
    type = models.ForeignKey(Type,verbose_name='漏洞分类',related_name='type_for_advancevuln',null=True,blank=True,on_delete=models.SET_NULL)
    level = models.ForeignKey(LEVEL,verbose_name='漏洞分级',related_name='level_for_advancevuln',null=True,blank=True,on_delete=models.SET_NULL)
    introduce = models.TextField('漏洞简介',null=True)
    fix = models.TextField('修复方案',null=True)
    create_data = models.DateTimeField('发现时间',auto_now_add=True)
    update_data = models.DateTimeField('修复时间',auto_now=True)
    
    def __str__(self):
        return self.vuln_name
    
    class Meta: 
        verbose_name = 'AdvanceVuln' 
        verbose_name_plural = '漏洞过滤' 
