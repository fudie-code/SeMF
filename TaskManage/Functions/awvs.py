#coding:utf-8
'''
Created on 2019年7月5日

@author: 残源
'''

import time 

from AdvanceManage.Functions import awvs11
from AdvanceManage.Functions import parse_awvs_xml
from VulnManage.models import Vuln,STATUS
from TaskManage.models import Task
from AssetManage.models import Asset
from SeMF.settings import TMP_PATH
from VulnManage.Functions import exceptvuln


vuln_level = {'informational':0,'low':1,'medium':2,'high':3}


def add_scan(scanner_id,url,desc):
    target_id = awvs11.add(url,scanner_id, desc)
    return target_id

def start_scan(scanner_id,target_id):
    data = awvs11.start(target_id,scanner_id)
    if data:
        scan_id = awvs11.getscanid(target_id,scanner_id)
    return scan_id

def stop_scan(scan_id,scanner_id):
    data = awvs11.stop(scan_id,scanner_id)
    if data:
        return True

def dele_scan(scan_id,scanner_id):
    data = awvs11.delete(scan_id,scanner_id)
    if data:
        return True

def get_scan_result(scan_id,task_id,scanner_id):
    reporturl = awvs11.getreport(scan_id,scanner_id)
    task = Task.objects.filter(task_id=task_id).first()
    parse_awvs_xml.get_scan_xml(reporturl,scan_id,TMP_PATH)
    details = parse_awvs_xml.details_parse_xml(scan_id,TMP_PATH)
    if details:
        asset_key = details['starturl']
        vuln_list = details['bug']
        asset =Asset.objects.filter(asset_key = asset_key).first()
        if vuln_list:
            except_vuln,except_vuln_list =  exceptvuln.Get_except_vuln('AWVS')
            for vuln in vuln_list:
                vuln_type = 'AWVS'
                vuln_name = vuln['name']
                leave = vuln_level[vuln['level']]
                vuln_info = vuln['request']
                introduce = vuln['details']
                scopen = vuln['path']
                fix = vuln['recommendation']
                if vuln_name in except_vuln:
                    vuln_gets = except_vuln_list.filter(vuln_name=vuln_name).first()
                    leave = vuln_gets.leave
                    fix = vuln_gets.fix
                vuln_list = Vuln.objects.get_or_create(name=vuln_name,
                                                     type=vuln_type,
                                                     level=leave,
                                                     introduce=introduce,
                                                     info=vuln_info,
                                                     scopen=scopen,
                                                     fix=fix,
                                                     asset = asset
                                                     )
                vuln_get = vuln_list[0]
                if vuln_list[1]:
                    if vuln_get.fix_status == STATUS.objects.filter(name='已修复').first():
                        vuln_get.fix_status= STATUS.objects.filter(name='漏洞重现').first()
                else:
                    if leave == 0:
                        vuln_get.fix_status= STATUS.objects.filter(name='已忽略').first()
                    elif leave == 1:
                        vuln_get.fix_status= STATUS.objects.filter(name='已忽略').first()
                    else:
                        vuln_get.fix_status= STATUS.objects.filter(name='待修复').first()
                vuln_get.task_id= task
                vuln_get.save()