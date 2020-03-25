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
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.documentation import include_docs_urls
# from rest_framework import routers
# from rest_framework.routers import DefaultRouter
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken import views      # drf登录
# from rest_framework_jwt.views import obtain_jwt_token   # JWT登录验证

from users.views import *
from vue_pms.views import MenuViewset, Config
from classification.views import Type, DaduiZhongduiTypeList, DiZhiList, CategoryTypeList, DiZhiNotListAll

router = DefaultRouter(trailing_slash=False)

router.register(r'PersonalInformationList', PersonalInformationList, basename='PersonalInformationList')    # 人员档案
router.register(r'Menu', MenuViewset, basename='Menu')  # 菜单
router.register(r'UserInformation', UserInformationList, basename='UserInformation')    # 账号
router.register(r'UserInformationNoneList', UserInformationNoneList, basename='UserInformationNoneList')    # 未关联档案账号
router.register(r'Type', Type, basename='Type')     # 分类数据
router.register(r'GroupList', GroupList, basename='GroupList')  # 用户组
# router.register(r'PermissionList', PermissionList, basename='PermissionList')   # 权限
router.register(r'DaduiZhongduiTypeList', DaduiZhongduiTypeList, basename='DaduiZhongduiTypeList')  # 大队、中队分类
router.register(r'DiZhiList', DiZhiList, basename='DiZhiList')  # 籍贯
router.register(r'DiZhiNotListAll', DiZhiNotListAll, basename='DiZhiNotListAll')
router.register(r'CategoryTypeList', CategoryTypeList, basename='CategoryTypeList')
router.register(r'DangTuanList', DangTuanList, basename='DangTuanList')
router.register(r'YongGongList', YongGongList, basename='YongGongList')
router.register(r'LvLiList', LvLiList, basename='LvLiList')
router.register(r'EducationList', EducationList, basename='EducationList')
router.register(r'CarList', CarList, basename='CarList')
router.register(r'HomeInformationList', HomeInformationList, basename='HomeInformationList')
router.register(r'PhysicalExaminationList', PhysicalExaminationList, basename='PhysicalExaminationList')
router.register(r'MeasureInformationList', MeasureInformationList, basename='MeasureInformationList')
router.register(r'ImgDataList', ImgDataList, basename='ImgDataList')
router.register(r'Config', Config, basename='网站设置')

urlpatterns = [
                  path('admin/', admin.site.urls),
                  re_path(r'^api-auth/', include('rest_framework.urls')),
                  re_path('docs/', include_docs_urls(title="信息管理系统")),
                  re_path('^', include(router.urls)),
                  # re_path('^api/v1/PersonalInformationList$', PersonalInformation_list, name='PIL'),
                  re_path('^Nation$', Nation.as_view(), name='Nation'),
                  re_path('^PermissionList$', PermissionList.as_view(), name='PermissionList'),
                  re_path('^TongJi$', TongJi.as_view(), name='TongJi'),
                  # re_path(r'^login', views.obtain_auth_token),       # drf自带token登录验证
                  re_path(r'^login', Login.as_view()),  # drf自带token登录验证
                  # re_path(r'^login', obtain_jwt_token),      # JWT登录验证
                  # re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
