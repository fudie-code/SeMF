#coding:utf-8
from django.db import models
from AssetManage.models import Type as AssetType

# Create your models here.
SCANNER_TYPE = (
                ('System',(
                           ('RSAS','RSAS'),
                           ('Nessus-sc','Nessus-sc'),
                           )
                 ),
                ('Web',(
                           ('RSAS','RSAS'),
                           ('AWVS','AWVS'),
                           )
                 ),
                )


class Scanner(models.Model):
    name = models.CharField('节点名称',max_length=50)
    type = models.CharField('节点类型',max_length=50,choices=SCANNER_TYPE)
    url = models.URLField('节点地址')
    status = models.BooleanField('节点状态',default=False)
    apikey = models.CharField('API_KEY',max_length=100)
    apisec = models.CharField('API_SEC',max_length=100,blank=True)
    description = models.TextField('节点描述')
    addtime = models.DateField('开始时间',auto_now_add=True)
    updatetime = models.DateField('结束时间',auto_now=True)
    
    assetType = models.ManyToManyField(AssetType,verbose_name='扫描范围',related_name='scanner_assettype')
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Scanner' 
        verbose_name_plural = '扫描节点' 
        

class Policies(models.Model):
    name = models.CharField('策略名称',max_length=50,help_text='扫描策略为扫描器策略名称')
    key = models.CharField('策略编号',max_length=50,null=True)
    scanner = models.ForeignKey(Scanner,verbose_name='节点关联',related_name='police_for_scanner',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Policies' 
        verbose_name_plural = '扫描策略' 