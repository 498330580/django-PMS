from django.shortcuts import render

# Create your views here.
# 引入同时渲染多个模型库
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from .serializers import *
from apps.classification.models import *


# from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions


# class CategoryTypeList(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """List:人员类别"""
#     queryset = CategoryType.objects.all()
#     serializer_class = CategoryTypeSerializer
#
#
# class DemobilizedTypeList(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """List:退伍军人类别"""
#     queryset = DemobilizedType.objects.all()
#     serializer_class = DemobilizedTypeSerializer
#
#
# class DrivingLicenseTypeList(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """List:驾照类别"""
#     queryset = DrivingLicenseType.objects.all()
#     serializer_class = DrivingLicenseTypeSerializer
#
#
# class DaDuiTypeList(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """List:大队类别"""
#     queryset = DaDuiType.objects.all()
#     serializer_class = DaDuiTypeSerializer
#
#
# class ZhongDuiTypeList(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """List:大队类别"""
#     queryset = ZhongDuiType.objects.all()
#     serializer_class = ZhongDuiTypeSerializer


class Type(ObjectMultipleModelAPIViewSet):
    """
        List:分类信息
    """
    permission_classes = (IsAuthenticated, )

    querylist = [
        {'queryset': CategoryType.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': DemobilizedType.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': DrivingLicenseType.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': DaDuiType.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': ZhongDuiType.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': Organization.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': Borrow.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': Economics.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': Sources.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': EducationType.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': AcademicDegreeType.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': CarType.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': PostType.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': PostName.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': XueLiInformation.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': RenYuanXianZhuang.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': ShenFenGuiLei.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': ChengWei.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': TiJianJieGuo.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': Year.objects.filter(is_delete=False), 'serializer_class': YearSerializer},
    ]
