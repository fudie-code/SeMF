#coding:utf-8
'''
Created on 2019年4月27日

@author: GY071
'''

from __future__ import absolute_import
from celery import shared_task

from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)
from . import models
from .Functions import scanneraction
from VulnManage import models as vulnmodel
from AssetManage import models as assetmodel
from TaskManage import models as taskmodel
import time


@shared_task
def get_rsas_vulns(task_id):
    task_get = models.Task.objects.filter(id =task_id).first()
    while True:
        status = scanneraction.statustask(task_get)
        if status == '4' or '8':
            #同步任务漏洞
            res = scanneraction.reporttask(task_get)
            if res:
                for item in res:
                    #type_get = vulnmodel.Type.objects.get_or_create(name=item['type'])
                    #ype_item = type_get[0]
                    res = vulnmodel.Vuln.objects.get_or_create(
                        name=item['name'],
                        level=vulnmodel.LEVEL.objects.filter(id=item['level']).first(),
                        asset = assetmodel.Asset.objects.filter(key = item['key']).first(),
                        type = vulnmodel.Type.objects.get_or_create(name=item['type'])[0],
                        )
                    if res:
                        asset_advance = vulnmodel.AdvanceVuln.objects.filter(vuln_name=item['name'],source__name='RSAS').first()
                        if asset_advance:
                            res = res[0]
                            res.fix_status = vulnmodel.STATUS.objects.filter(name="待修复").first()
                            res.info=item['info']
                            res.task= task_get
                            res.cve=item['cve']
                            res.type=asset_advance.type
                            res.level=asset_advance.level
                            res.introduce=asset_advance.introduce
                            res.fix=asset_advance.fix
                        else:
                            res = res[0]
                            res.fix_status = vulnmodel.STATUS.objects.filter(name="待修复").first()
                            res.info=item['info']
                            res.task= task_get
                            res.cve=item['cve']
                            res.introduce=item['introduce']
                            res.fix=item['fix']
                        res.save()
                task_get.status =taskmodel.STATUS.objects.filter(name='已完成').first()
                task_get.save()
                '''
                data_get={
                    'id':task_id,
                    'title':'任务执行通知',
                    'body':'您的扫描任务已完成，请前往任务列表查看勘界',
                    'url':'',
                    'user':task_get.user,
                }
                notice_service.savemessage(data_get)'''
                break
        elif status == '5':
            '''
            data_get={
                    'id':task_id,
                    'title':'任务执行通知',
                    'body':'您的扫描任务已暂停',
                    'url':'',
                    'user':task_get.user,
                }
            notice_service.savemessage(data_get)'''
            break
        else:
            time.sleep(60)