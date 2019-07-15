#coding:utf-8
from __future__ import absolute_import
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app
__all__ = ['celery_app']
#mysqlclient.install_as_MySQLdb()