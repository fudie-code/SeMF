#coding:utf-8
'''
Created on 2017/11/10

@author: gy
'''
from AdvanceManage.Functions import nessus6
import time
from VulnManage.models import Vuln,STATUS
from AssetManage.models import Asset,Type
from VulnManage.Functions import exceptvuln



def add_nessus_scan(name,introduce,target,scanner_id,police):
    policies = nessus6.get_policies(scanner_id)
    pid = policies[police]
    scan = nessus6.add(name,introduce,target,pid,scanner_id)
    scan_id=scan['id']
    return scan_id

def launch_nessus_scan(scan_id,scanner_id):
    scan_uuid=nessus6.launch(scan_id,scanner_id)
    return scan_uuid

def pause_nessus_scan(scan_id,scanner_id):
    scan_uuid = nessus6.pause(scan_id,scanner_id)
    return scan_uuid

def resume_nessus_scan(scan_id,scanner_id):
    scan_uuid = nessus6.resume(scan_id,scanner_id)
    return scan_uuid

def stop_nessus_scan(scan_id,scanner_id):
    scan_uuid = nessus6.stop(scan_id,scanner_id)
    return scan_uuid

def get_scan_status(scan_id,scanner_id):
    res = nessus6.details(scan_id,scanner_id)
    return res['info']['status']

def get_scan_vuln(scan_id,task,scanner_id):
    res = nessus6.details(scan_id,scanner_id)
    vuln_list = res.get('vulnerabilities')
    asset_type = Type.objects.filter(name = '服务器').first()
    if vuln_list:
        except_vuln,except_vuln_list = exceptvuln('Nessus')
        for vuln in vuln_list:
            for host in res['hosts']:
                host_id = host['host_id']
                hostname = host['hostname']
                asset_get = Asset.objects.get_or_create(asset_key=hostname)
                asset=asset_get[0]
                if asset_get[1]:
                    asset_host=asset
                    try:
                        num_id =Asset.objects.latest('id').id
                    except:
                        num_id = 0
                    num_id += 1
                    asset_id = '01' + time.strftime('%Y%m%d',time.localtime(time.time()))+str(num_id)
                    asset_name = '服务器-' + asset_id
                    asset_host.asset_id=asset_id
                    asset_host.asset_name=asset_name
                    asset_host.asset_type=asset_type
                    asset_host.save()
                else:
                    pass
                    
                try:
                    num = Vuln.objects.latest('id').id
                except Exception as e:
                    num = 0
                vuln_id ='01'+ str(time.strftime('%Y%m%d%H',time.localtime(time.time()))) + str(num)
                vuln_type = 'Nessus'
                vuln_name = vuln.get('plugin_name')
                out_details = nessus6.get_plugin_output(scan_id, host_id, vuln['plugin_id'],scanner_id)
                vuln_info = out_details.get('outputs')
                if vuln_info:
                    if vuln_name in except_vuln:
                        vuln_gets = except_vuln_list.filter(vuln_name=vuln_name).first()
                        leave = vuln_gets.leave 
                        fix = vuln_gets.fix
                    else:
                        leave = vuln.get('severity')
                        fix = out_details['info']['plugindescription']['pluginattributes']['solution']
                    introduce = out_details['info']['plugindescription']['pluginattributes']['description']
                    scopen = hostname
                    
                    vuln_list = Vuln.objects.get_or_create(vuln_name=vuln_name,
                                                                         vuln_type=vuln_type,
                                                                         leave=leave,
                                                                         introduce=introduce,
                                                                         vuln_info=vuln_info,
                                                                         scopen=scopen,
                                                                         fix=fix,
                                                                         vuln_asset = asset
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
