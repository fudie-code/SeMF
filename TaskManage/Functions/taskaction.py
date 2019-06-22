#coding:utf-8
'''
Created on 2019年6月22日

@author: 残源
'''
from TaskManage import models as taskmodels



def task_action(task_obj,action):
    data = {
        'status':False,
        'msg':''
        }
    if action == 'start':
        res = True
        if res:
            data['status']=True
            task_obj.status = taskmodels.Task.objects.filter(name ='执行中').first()
    elif action == 'stop':
        res = True
        if res:
            data['status']=True
            task_obj.status = taskmodels.Task.objects.filter(name ='已完成').first()
    elif action == 'pause':
        res = True
        if res:
            data['status']=True
            task_obj.status = taskmodels.Task.objects.filter(name ='已暂停').first()
    elif action == 'resume':
        res = True
        if res:
            data['status']=True
            task_obj.status = taskmodels.Task.objects.filter(name ='执行中').first()
    else:
        data['msg'] = '参数不合法'
    task_obj.save()
    return data
        