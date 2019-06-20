#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import django.utils.timezone as timezone
#from AssetManage import models as assetmodels

# Create your models here.
        
        
class Menu(models.Model):
    order = models.IntegerField('排序',default = 0)
    name = models.CharField(verbose_name = '菜单名称',max_length = 100)
    key = models.CharField(verbose_name = '菜单标识',max_length = 50)
    icon = models.CharField(verbose_name = '菜单图标',max_length = 100)
    jump = models.CharField(verbose_name = '跳转地址',max_length = 200,null=True,blank=True)
    parent = models.ForeignKey('self',verbose_name = '上级菜单',related_name='menu_menu',null=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        title_list = [self.name]
        p=self.parent
        while p:
            title_list.insert(0,p.name)
            p = p.parent
        return '-'.join(title_list)
    
    class Meta: 
        verbose_name = 'Menu' 
        verbose_name_plural = '菜单管理' 


class Permission(models.Model):
    name = models.CharField(verbose_name = '权限名称',max_length = 100)
    url = models.CharField(verbose_name = '授权地址',max_length=200)
    menu = models.ForeignKey(Menu,verbose_name = '菜单关联',related_name='permission_menu',null=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Permission' 
        verbose_name_plural = '权限关联' 
        

class Role(models.Model):
    name = models.CharField('角色名称',max_length=25,unique=True)
    description = models.TextField('角色描述',null=True,blank=True)
    menu = models.ManyToManyField(Menu,verbose_name='角色关联',related_name='role_menu')
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Role' 
        verbose_name_plural = '角色管理' 


class UserResetpsd(models.Model):
    email = models.EmailField('邮箱地址')
    urlarg = models.CharField('校验参数',max_length=50)
    is_check = models.BooleanField('是否审批',default=False)
    is_start = models.BooleanField('是否有效',default=False)
    updatetime = models.DateField('更新时间',auto_now=True)
    user = models.ForeignKey(User,verbose_name='申请人',related_name='reseppsd_user',on_delete=models.CASCADE,)
    def __str__(self):
        return self.email
    
    class Meta: 
        verbose_name = 'UserResetpsd' 
        verbose_name_plural = '操作校验' 


        
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    title =  models.CharField('职位名称',max_length=50,null=True,blank=True)
    
    is_resetpsd = models.BooleanField('强制修改密码',default=True)
    
    mobilephone = models.CharField('手机号码',max_length=50)
    error_count = models.IntegerField('错误登录',default=0)
    login_count = models.IntegerField('登录统计',default=0)
    lock_time = models.DateTimeField('锁定时间',default = timezone.now)
    
    parent = models.ManyToManyField(User,verbose_name='汇报对象',blank=True,related_name='user_parent')
    
    roles = models.ManyToManyField(Role,verbose_name='管理人员',related_name='user_role')
    
    def __str__(self):
        return self.user.username
    
    class Meta: 
        verbose_name = 'Profile' 
        verbose_name_plural = '用户属性' 
 
@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
        Profile.objects.get_or_create(user=instance)  

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
