#coding:utf-8
'''
Created on 2018年11月8日

@author: 残源
'''

import django,os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SecurityEvaluationManage.settings')
django.setup()
from RBAC.models import Permission,Menu,Role
from AssetManage import models as assetmodels
from VulnManage import models as vulnmodels


def initmenu():
    menu_list = [
         {'name':'资产管理','key':'assetmanage','icon':"layui-icon-form",'jump':'','parent':''},
         {'name':'项目列表','key':'rootlist','icon':"",'jump':'assetmanage/rootlist','parent':'assetmanage'},
         {'name':'资产列表','key':'list','icon':"",'jump':'assetmanage/list','parent':'assetmanage'},
         '''
         {'name':'漏洞管理','key':'vulnmanage','icon':"layui-icon-template",'jump':'','parent':''},
         {'name':'漏洞列表','key':'list','icon':"",'jump':'vulnmanage/list','parent':'vulnmanage'},
         
         {'name':'任务管理','key':'taskmanage','icon':"layui-icon-template-1",'jump':'','parent':''},
         {'name':'任务列表','key':'list','icon':"",'jump':'taskmanage/list','parent':'taskmanage'},
         
         {'name':'评测管理','key':'evaluationmanage','icon':"layui-icon-app",'jump':'','parent':''},
         {'name':'评测列表','key':'list','icon':"",'jump':'evaluationmanage/list','parent':'evaluationmanage'},
         
         #{'name':'知识库','key':'articlemanage','icon':"layui-icon-read",'jump':'','parent':''},
         #{'name':'知识库列表','key':'list','icon':"",'jump':'articlemanage/list','parent':'articlemanage'},
         
         {'name':'用户管理','key':'administrators','icon':"layui-icon-user",'jump':'','parent':''},
         {'name':'用户列表','key':'list','icon':"",'jump':'administrators/list','parent':'administrators'},
         {'name':'企业列表','key':'company','icon':"",'jump':'administrators/company','parent':'administrators'},

         {'name':'通告管理','key':'noticemanage','icon':"layui-icon-speaker",'jump':'','parent':''},
         {'name':'通告列表','key':'list','icon':"",'jump':'noticemanage/list','parent':'noticemanage'},
         
         
         {'name':'系统设置','key':'set','icon':"layui-icon-set",'jump':'','parent':''},
         {'name':'我的设置','key':'user','icon':"",'jump':'','parent':'set'},
         {'name':'修改密码','key':'password','icon':"",'jump':'set/user/password','parent':'user'},
         {'name':'企业信息','key':'company','icon':"",'jump':'set/user/company','parent':'user'},

         {'name':'知识库','key':'article','icon':"layui-icon-read",'jump':'','parent':''},
         {'name':'文章管理','key':'list','icon':"",'jump':'article/list','parent':'article'},
         {'name':'文章列表','key':'artlist','icon':"",'jump':'article/artlist','parent':'article'}'''
         ]
    for item in menu_list:
        menu_get = Menu.objects.get_or_create(
            name=item['name']
            ,key=item['key']
            ,icon=item['icon']
            ,jump=item['jump']
            )
        menu_get = menu_get[0]
        menu_get.parent= Menu.objects.filter(key=item['parent']).first()
        menu_get.save()
    print('initmenu OK')
    
def initPermission():
    #权限对应的菜单均为第一级菜单，情确保访问该菜单相关页面url均已授权至菜单
    permission_list =[
        {'name':'用户管理','url':'/super/','menu':'administrators'},
        
        ]
    for item in permission_list:
        permission_get = Permission.objects.get_or_create(
            name=item['name'],
            url=item['url'],
            )
        permission_get = permission_get[0]
        permission_get.menu = Menu.objects.filter(key=item['menu']).first()
        permission_get.save()
    print('initPermission OK')
    
def initRole():
    role_list=[
        {'name':'普通账号','description':'系统基本使用权限','menu':['asset','vuln','task','set']},
        {'name':'管理账号','description':'普通管理权限','menu':['administrators']},
        ]
    for item in role_list:
        role_get = Role.objects.get_or_create(name=item['name'])
        role_get=role_get[0]
        role_get.description=item['description']
        for menu_get in Menu.objects.filter(key__in=item['menu']):
            role_get.menu.add(menu_get)
        role_get.save()
    print('initRole ok')

    
def initassettype():
    type_list=[
        {'name':'企业项目','is_root':False,'description':'虚拟资产项目分类，用于作为合规评测主体','parent':''},
        {'name':'服务器','is_root':False,'description':'具象化资产','parent':''},
        {'name':'WEB应用','is_root':False,'description':'WEB服务','parent':''},
        {'name':'数据库','is_root':False,'description':'系统数据库','parent':''},
        #{'name':'其他','is_root':False,'description':'其他资产，未加定义','parent':''},
        ]
    for item in type_list:
        item_get = assetmodels.Type.objects.get_or_create(name=item['name'])
        item_get=item_get[0]
        item_get.is_root=item['is_root']
        item_get.description=item['description']
        item_get.parent =assetmodels.Type.objects.filter(name=item['parent']).first()
        item_get.save()
    print('initassettype ok')
    
def initassettypeinfo():
    type_list=[
        {'key':'sql','name':'数据库属性','type_connect':['数据库',]},
        {'key':'web','name':'网站属性','type_connect':['WEB应用',]},
        {'key':'plugin','name':'组件属性','type_connect':['WEB应用']},
        {'key':'os','name':'操作系统属性','type_connect':['服务器',]},
        {'key':'port','name':'端口属性','type_connect':['服务器',]},
        {'key':'file','name':'文件属性','type_connect':['企业项目','服务器','WEB应用','数据库']},
        ]
    for item in type_list:
        item_get = assetmodels.TypeInfo.objects.get_or_create(name=item['name'],key=item['key'])
        item_get=item_get[0]
        for type_get in assetmodels.Type.objects.filter(name__in=item['type_connect']):
            item_get.type_connect.add(type_get)
        item_get.save()
    print('initassettypeinfo ok')

def initsqltype():
    type_list=[
        {'name':'Other'},
        {'name':'SQLServer'},
        {'name':'mysql'},
        {'name':'Oracle'},
        {'name':'Sybase'},
        {'name':'DB2'},
        {'name':'Postgresql'},
        {'name':'Mongodb'},
        {'name':'Redis'},
        {'name':'Hbase'},
        ]
    for item in type_list:
        item_get = assetmodels.SQLType.objects.get_or_create(name=item['name'])
    print('initsqltype ok')

def initostype():
    type_list=[
        {'name':'Other'},
        {'name':'winserver2008'},
        {'name':'winserver2012'},
        {'name':'winserver2016'},
        {'name':'centos'},
        {'name':'Ubuntu'},
        {'name':'Debian'},
        {'name':'RedHat'},
        ]
    for item in type_list:
        item_get = assetmodels.OSType.objects.get_or_create(name=item['name'])
    print('initostype ok')

def initLanguageType():
    type_list=[
        {'name':'Other'},
        {'name':'C/C++'},
        {'name':'C#'},
        {'name':'Ruby'},
        {'name':'JAVA'},
        {'name':'ASP.NET'},
        {'name':'JSP'},
        {'name':'PHP'},
        {'name':'Perl'},
        {'name':'Python'},
        {'name':'VB.NET'},
        ]
    for item in type_list:
        item_get = assetmodels.LanguageType.objects.get_or_create(name=item['name'])
    print('initLanguageType ok')

'''def initVulnLevel():
    type_list=[
        {'name':'信息'},
        {'name':'低危'},
        {'name':'中危'},
        {'name':'高危'},
        {'name':'紧急'},
        ]
    for item in type_list:
        item_get = vulnmodels.LEVEL.objects.get_or_create(name=item['name'])
    print('initVulnLevel ok')
    
def initVulnStatus():
    type_list=[
        {'name':'待修复'},
        {'name':'已忽略'},
        {'name':'已修复'},
        {'name':'暂缓修复'},
        {'name':'漏洞重现'},
        {'name':'系统误报'},
        ]
    for item in type_list:
        item_get = vulnmodels.STATUS.objects.get_or_create(name=item['name'])
    print('initVulnStatus ok')


def initVulnType():
    type_list=[
        {'name':'系统漏洞'},
        {'name':'应用漏洞'},
        ]
    for item in type_list:
        item_get = vulnmodels.Type.objects.get_or_create(name=item['name'])
    print('initVulnType ok')
    
    
def initTaskStatus():
    type_list=[
        {'name':'待执行'},
        {'name':'执行中'},
        {'name':'已暂停'},
        {'name':'已完成'},
        ]
    for item in type_list:
        item_get = taskmodels.STATUS.objects.get_or_create(name=item['name'])
    print('initTaskStatus ok')

    
def initArticleStatus():
    type_list=[
        {'name':'新建'},
        {'name':'审核'},
        {'name':'发布'},
        ]
    for item in type_list:
        item_get = articlemodels.STATUS.objects.get_or_create(name=item['name'])
    print('initArticleStatus ok')

def initArticleType():
    type_list=[
        {'name':'知识库类型1'},
        {'name':'知识库类型2'},
        {'name':'知识库类型3'},
        ]
    for item in type_list:
        item_get = articlemodels.Type.objects.get_or_create(name=item['name'])
    print('initArticleType ok')

def initNoticeStatus():
    type_list=[
        {'name':'草稿'},
        {'name':'发布'},
        ]
    for item in type_list:
        item_get = noticemodels.STATUS.objects.get_or_create(name=item['name'])
    print('initNoticeStatus ok')'''

if __name__ == "__main__":
    initmenu()
    initPermission()
    initRole()
    initassettype()
    initassettypeinfo()
    initsqltype()
    initostype()
    initLanguageType()
    '''initVulnLevel()
    initVulnStatus()
    initVulnType()
    initTaskStatus()
    initArticleStatus()
    initArticleType()
    initNoticeStatus()'''
