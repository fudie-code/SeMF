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
from AdvanceManage.Functions import awvs11,nessus6
from .Functions import awvs,nessus
import time


@shared_task
def save_awvs_vulns(scan_id,task_id):
    task = models.Task.objects.filter(task_id =task_id ).first()
    while True:
        status = awvs11.getstatus(scan_id,task.task_scanner.id)
        if status == 'completed':
            awvs.get_scan_result(scan_id,task_id,task.task_scanner.id)
            task.task_status=models.STATUS.objects.filter(name= '已完成').first()
            task.save()
            break
        elif status == 'aborted':
            awvs.get_scan_result(scan_id,task_id,task.task_scanner.id)
            task.task_status=models.STATUS.objects.filter(name= '已完成').first()
            task.save()
            break
        else:
            time.sleep(60)
            
            
@shared_task
def save_nessus_vulns(scan_id,task_id):
    task = models.Task.objects.filter(task_id =task_id ).first()
    while True:
        res = nessus6.details(scan_id,task.task_scanner.id)
        try:
            res['info']['status']
        except:
            continue
        if res['info']['status'] == 'canceled' or res['info']['status'] == 'completed':
            time.sleep(600)
            nessus.get_scan_vuln(scan_id,task,task.task_scanner.id)
            task.task_status=models.STATUS.objects.filter(name= '已完成').first()
            task.save()
            break
        else:
            time.sleep(30)