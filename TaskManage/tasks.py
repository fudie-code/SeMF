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
from AdvanceManage.Functions import awvs11
from .Functions import awvs
import time


@shared_task
def save_awvs_vulns(scan_id,task_id):
    task = models.Task.objects.filter(task_id =task_id ).first()
    while True:
        status = awvs11.getstatus(scan_id,task.task_scanner.id)
        if status == 'completed':
            awvs.get_scan_result(scan_id,task_id,task.task_scanner.id)
            task.task_status=4
            task.save()
            break
        elif status == 'aborted':
            awvs.get_scan_result(scan_id,task_id,task.task_scanner.id)
            task.task_status=5
            task.save()
            break
        else:
            time.sleep(60)