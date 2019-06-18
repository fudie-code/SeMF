#coding:utf-8
from django.contrib import admin

# Register your models here.
from AssetManage import models

admin.site.register(models.Type)
admin.site.register(models.Asset)
admin.site.register(models.OsInfo)
admin.site.register(models.WebInfo)
admin.site.register(models.PortInfo)
admin.site.register(models.PluginInfo)
admin.site.register(models.File)