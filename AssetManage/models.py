#coding:utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Type(models.Model):
    name = models.CharField('分类名称',max_length = 50)
    is_root = models.BooleanField('主节点',default=False)
    description = models.TextField('分类描述')
    parent = models.ForeignKey('self',verbose_name='上级分类',related_name='assettype_type',null=True,blank=True,on_delete=models.SET_NULL)
    
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
        verbose_name_plural = '资产分类' 

class TypeInfo(models.Model):
    key = models.CharField('属性标识',max_length = 30,null=True)
    name = models.CharField('资产属性',max_length = 30)
    type_connect = models.ManyToManyField(Type,verbose_name='属性关联',related_name='typeinfo_assettype',blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'TypeInfo' 
        verbose_name_plural = '资产信息' 
    
    
    
class Asset(models.Model):
    name = models.CharField('资产名称',max_length= 100)
    key = models.CharField('唯一标识',max_length= 100,unique=True)
    type = models.ForeignKey(Type,related_name='type_for_asset',verbose_name='资产类型',on_delete=models.SET_NULL,null=True)
    description = models.TextField('资产说明',null=True,blank=True)
    is_delete = models.BooleanField('是否删除',default=False)
    weight = models.IntegerField('权重1-n',default=1)
    
    manage = models.CharField('负责人',max_length = 100,null=True,blank=True)
    telephone = models.CharField('负责人电话',max_length=50,null=True,blank=True)
    email = models.EmailField('负责人邮箱',null=True,blank=True)
    user = models.ManyToManyField(User,related_name='asset_for_user',verbose_name='所属用户',blank=True)
    
    starttime = models.DateTimeField('添加时间',auto_now_add=True)
    updatetime = models.DateTimeField('更新时间',auto_now=True)
    
    parent = models.ManyToManyField('self',verbose_name='资产关联',related_name='asset_connect',blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Asset' 
        verbose_name_plural = '资产管理' 
        
        
class SQLType(models.Model):
    name = models.CharField('数据库类型',max_length= 100)
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'SQLType' 
        verbose_name_plural = '数据库类型' 



class SQLInfo(models.Model):
    key = models.CharField('访问地址',null=True,blank=True,max_length= 100)
    os = models.ForeignKey(SQLType,verbose_name='数据库分类',related_name='type_sql',null=True,blank=True,on_delete=models.SET_NULL)
    version = models.CharField('数据库版本',max_length=50,blank=True,null=True)
    cycle = models.CharField('备份周期',max_length=50,blank=True,null=True)
    updatetime = models.DateTimeField('更新时间',auto_now=True)
    
    asset = models.ForeignKey(Asset,related_name='sql_for_asset',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.key
    
    class Meta: 
        verbose_name = 'OsInfo' 
        verbose_name_plural = '数据库信息' 



class OSType(models.Model):
    name = models.CharField('操作系统类型',max_length= 100)
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'OSType' 
        verbose_name_plural = '操作系统类型' 


class OsInfo(models.Model):
    key = models.CharField('IP地址',null=True,blank=True,max_length= 100)
    hostname = models.CharField(max_length=50, verbose_name="主机名")
    os = models.ForeignKey(OSType,verbose_name='操作系统',related_name='type_os',null=True,blank=True,on_delete=models.SET_NULL)
    cpu_num = models.CharField("CPU数量", max_length=100, blank=True)
    memory = models.CharField("内存大小", max_length=30, blank=True)
    disk = models.CharField("硬盘大小", max_length=255, blank=True)
    updatetime = models.DateTimeField('更新时间',auto_now=True)
    
    asset = models.OneToOneField(Asset,related_name='os_for_asset',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.key
    
    class Meta: 
        verbose_name = 'OsInfo' 
        verbose_name_plural = '服务器信息' 

class LanguageType(models.Model):
    name = models.CharField('操作系统类型',max_length= 100)
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'OSType' 
        verbose_name_plural = '编程语言'        

class WebInfo(models.Model):
    key = models.CharField('域名地址',null=True,blank=True,max_length= 100)
    middleware = models.CharField('中间件',max_length=50,blank=True,null=True)
    middleware_version = models.CharField('版本',max_length=50,blank=True,null=True)
    language = models.ForeignKey(LanguageType,verbose_name='编程语言',related_name='type_language',null=True,blank=True,on_delete=models.SET_NULL)
    web_framwork = models.CharField('开发框架',max_length = 50,blank=True,null=True)
    web_framwork_version = models.CharField('开发框架版本',max_length = 50,blank=True,null=True)
    updatetime = models.DateTimeField('更新时间',auto_now=True)
    asset = models.OneToOneField(Asset,related_name='web_for_asset',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.key
    
    class Meta: 
        verbose_name = 'WebInfo' 
        verbose_name_plural = '网站信息'
        
        
class PortInfo(models.Model):
    port = models.CharField('开放端口',max_length=50)
    name = models.CharField('服务名称',max_length=50,null=True,blank=True)
    product = models.CharField('产品信息',max_length=100,null=True,blank=True)
    version = models.CharField('应用版本',max_length=50,null=True,blank=True)
    port_info = models.TextField('端口介绍',null=True,blank=True)
    updatetime = models.DateTimeField('更新时间',auto_now=True)
    is_delete = models.BooleanField('是否删除',default=False)
    
    asset = models.ForeignKey(Asset,related_name='port_for_asset',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.port
    
    class Meta: 
        verbose_name = 'PortInfo' 
        verbose_name_plural = '端口信息'


        
class PluginInfo(models.Model):
    name = models.CharField('组件名称',max_length=50)
    version = models.CharField('应用版本',max_length=50,null=True)
    plugin_info = models.TextField('组件简介',null=True)
    starttime = models.DateTimeField('添加时间',auto_now_add=True)
    updatetime = models.DateTimeField('更新时间',auto_now=True)
    is_delete = models.BooleanField('是否删除',default=False)
    
    asset = models.ForeignKey(Asset,related_name='plugin_for_asset',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'PluginInfo' 
        verbose_name_plural = '组件信息'
    
    
class File(models.Model):
    name = models.CharField('附件名称',max_length=200)
    type  = models.CharField('文件类型',max_length =100)
    file = models.FileField('附件内容',upload_to ='assetfiles/%Y/%m/%d/')
    file_info = models.TextField('附件说明',null=True)
    updatetime = models.DateTimeField('更新时间',auto_now=True)
    
    asset = models.ForeignKey(Asset,related_name='file_for_asset',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'File' 
        verbose_name_plural = '文件信息'
    