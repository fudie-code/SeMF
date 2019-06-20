#coding:utf-8
from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Type)
admin.site.register(models.STATUS)
admin.site.register(models.LEVEL)
admin.site.register(models.Vuln)
admin.site.register(models.Source)
admin.site.register(models.AdvanceVuln)