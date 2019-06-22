"""SeMF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('csrf/',views.get_token,name='csrf'),
    
    
    path('rbac/',include('RBAC.urls')),
    path('asset/',include('AssetManage.urls')),
    path('vuln/',include('VulnManage.urls')),
    path('task/',include('TaskManage.urls')),
    path('user/',include('UserManage.urls')),
    path('article/',include('ArticleManage.urls')),
    path('notice/',include('NoticeManage.urls')),
    
    path('semf/', admin.site.urls),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
