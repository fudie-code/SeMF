#coding:utf-8
'''
Created on 2019年7月1日

@author: 残源
'''

from AdvanceManage.Functions import nmap
from .. import models



def check_asset_all_port(asset_obj):
    
    port_list = nmap.nmap_host_all(asset_obj.key)
    if port_list!=0:
        for port_info in port_list.keys():
            port = port_info
            name = port_list[port_info].get('name')
            product = port_list[port_info].get('product')
            version =  port_list[port_info].get('version')
            port_get = models.PortInfo.objects.get_or_create(
                port=port,
                asset = asset_obj,
                )
            if port_get[1]:
                port = port_get[0]
                port.product=product
                port.name = name
                port.version=version
                port.save()
            