#coding:utf-8
'''
Created on 2019年6月22日

@author: 残源
'''

from .. import models



def vuln_check(vuln_list):
    '''
    data=[
            {'name':'',
            'source':'',
            'cve':'',
            'type':'',
            'level':'',
            'introduce':'',
            'info':'',
            'scopen':'',
            'fix':'',
            }]
    '''
    check_list=[]
    for vuln_item in vuln_list:
        name = vuln_item.name
        source = vuln_item.source
        advancevuln_get = models.AdvanceVuln.objects.filter(name=name,source__name = source).order_by('update_data').first()
        if advancevuln_get:
            vuln_item.name = advancevuln_get.vuln_name
            vuln_item.source = advancevuln_get.source
            vuln_item.type = advancevuln_get.type
            vuln_item.level = advancevuln_get.level
            vuln_item.introduce = advancevuln_get.introduce
            vuln_item.fix = advancevuln_get.fix
        check_list.append(vuln_item)
    return check_list
        
        
        