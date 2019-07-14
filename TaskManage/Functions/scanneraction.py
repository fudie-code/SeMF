#coding:utf-8
'''
Created on 2019年4月27日

@author: GY071
'''

from ..tasks import save_awvs_vulns,save_nessus_vulns
from .. import models
from . import awvs,nessus

def create_start_task(task_get):
    if task_get.scanner.type == 'AWVS':
        for asset_item in task_get.asset.all():
            target = asset_item.key
        scan_id = awvs.add_scan(task_get.scanner.id, target, task_get.targetinfo)
        scan_id = awvs.start_scan(task_get.scanner.id,scan_id)
        if scan_id:
            status_get = models.STATUS.objects.filter(name='执行中').first()
            task_get.status = status_get
            task_get.scan_id = scan_id
            task_get.save()
            save_awvs_vulns.delay(scan_id,task_get.task_id)
            return True
    elif task_get.scanner.type == 'Nessus':
        for asset_item in task_get.asset.all():
            target = asset_item.key
        scan_id = nessus.add_nessus_scan(task_get.name,task_get.targetinfo,target,task_get.scanner.id,task_get.police.name)
        do_res = nessus.launch_nessus_scan(scan_id,task_get.scanner.id)
        if do_res:
            status_get = models.STATUS.objects.filter(name='执行中').first()
            task_get.status = status_get
            task_get.scan_id = scan_id
            task_get.save()
            save_nessus_vulns.delay(scan_id,task_get.task_id)
            return True
    return False
        


def pasuetask(task_get):
    if task_get.scanner.type == 'AWVS':
        return False
    elif task_get.scanner.type == 'Nessus':
        do_res = nessus.pause_nessus_scan(task_get.scan_id,task_get.scanner.id)
        if do_res:
            status_get = models.STATUS.objects.filter(name='已暂停').first()
            task_get.status = status_get
            task_get.save()
            return True
    return False


def resumetask(task_get):
    if task_get.scanner.type == 'AWVS':
        return False
    elif task_get.scanner.type == 'Nessus':
        do_res = nessus.resume_nessus_scan(task_get.scan_id,task_get.scanner.id)
        if do_res:
            status_get = models.STATUS.objects.filter(name='执行中').first()
            task_get.status = status_get
            task_get.save()
            return True
    return False

def stoptask(task_get):
    if task_get.scanner.type == 'AWVS':
        res = awvs.stop_scan(task_get.scan_id,task_get.task_scanner.id)
        if res.get('status'):
            status_get = models.STATUS.objects.filter(name='已完成').first()
            task_get.status = status_get
            task_get.save()
            return True
    elif task_get.scanner.type == 'Nessus':
        do_res = nessus.resume_nessus_scan(task_get.scan_id,task_get.scanner.id)
        if do_res:
            status_get = models.STATUS.objects.filter(name='已完成').first()
            task_get.status = status_get
            task_get.save()
            return True
    return False




    