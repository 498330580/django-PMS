"""PMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path, include

from rest_framework.documentation import include_docs_urls
# from rest_framework import routers
# from rest_framework.routers import DefaultRouter
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views      # drf登录
# from rest_framework_jwt.views import obtain_jwt_token   # JWT登录验证

from users.views import PersonalInformationList

router = DefaultRouter(trailing_slash=False)

router.register(r'PersonalInformationList', PersonalInformationList, basename='PersonalInformationList')

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    path('docs/', include_docs_urls(title="信息管理系统")),
    path('api/', include(router.urls)),
    # re_path('^api/v1/PersonalInformationList$', PersonalInformation_list, name='PIL'),
    re_path(r'^api-token-auth', views.obtain_auth_token),       # drf自带token登录验证
    # re_path(r'^login', obtain_jwt_token),      # JWT登录验证

]
