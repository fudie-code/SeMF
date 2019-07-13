#coding:utf-8
'''
Created on 2019年4月27日

@author: GY071
'''


def rasacreateinfo(task_get):
    info = {
        'base_url':'',
        'username':'',
        'password':'',
        'name':'',
        'target':'',
        'template_id':'',
        }
    
    info['base_url'] = task_get.scanner.url
    info['username'] = task_get.scanner.apikey
    info['password']= task_get.scanner.apisec
    info['name'] = task_get.name
    info['target'] = task_get.target
    info['template_id'] = task_get.police.key
    
    return info


def rsasactioninfo(task_get):
    info = {
        'base_url':'',
        'username':'',
        'password':'',
        'task_id':'',
        'targets':'',
        }
    info['base_url'] = task_get.scanner.url
    info['username'] = task_get.scanner.apikey
    info['password']= task_get.scanner.apisec
    info['task_id'] = task_get.scan_id
    
    return info
    