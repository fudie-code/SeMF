#coding:utf-8
'''
Created on 2019年4月27日

@author: GY071
'''

from . import baseinfo
from SeMF.views import checkips
from .. import models,tasks

def create_start_task(task_get):
    if task_get.scanner.type == 'RSAS':
        post_data = baseinfo.rasacreateinfo(task_get)
        if checkips(task_get.target):
            #res = rsas.create_vulnerabilities_scan_task(post_data)
            res=1
        else:
            #res = rsas.create_web_scan_task(post_data)
            res=1
        if res.get('status'):
            status_get = models.STATUS.objects.filter(name='执行中').first()
            task_get.status = status_get
            task_get.scan_id = res.get('scan_id')
            task_get.save()
            tasks.get_rsas_vulns.delay(task_get.id)
            return True
    return False
        


def pasuetask(task_get):
    if task_get.scanner.type == 'RSAS':
        post_data = baseinfo.rsasactioninfo(task_get)
        #res = rsas.task_pause(post_data)
        res=1
        if res.get('status'):
            status_get = models.STATUS.objects.filter(name='已暂停').first()
            task_get.status = status_get
            task_get.save()
            return True
    return False


def resumetask(task_get):
    if task_get.scanner.type == 'RSAS':
        post_data = baseinfo.rsasactioninfo(task_get)
        #res = rsas.task_resume(post_data)
        res=1
        if res.get('status'):
            status_get = models.STATUS.objects.filter(name='执行中').first()
            task_get.status = status_get
            task_get.save()
            tasks.get_rsas_vulns.delay(task_get.id)
            return True
    return False

def stoptask(task_get):
    if task_get.scanner.type == 'RSAS':
        post_data = baseinfo.rsasactioninfo(task_get)
        #res = rsas.task_stop(post_data)
        res=1
        if res.get('status'):
            status_get = models.STATUS.objects.filter(name='已结束').first()
            task_get.status = status_get
            task_get.save()
            return True
    return False


def statustask(task_get):
    if task_get.scanner.type == 'RSAS':
        post_data = baseinfo.rsasactioninfo(task_get)
        #res = rsas.task_status(post_data)
        res=1
        if res.get('status'):
            return res.get('scan_status')
    return False

def reporttask(task_get):
    if task_get.scanner.type == 'RSAS':
        post_data = baseinfo.rsasactioninfo(task_get)
        #res = rsas.task_report(post_data)
        res=1
        if res.get('status'):
            return res.get('data')
    return False



    