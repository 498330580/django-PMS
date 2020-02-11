from django.shortcuts import render

# Create your views here.
# 引入同时渲染多个模型库
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication

from rest_framework import viewsets
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend

from classification.serializers import *
from classification.models import *
from classification.fiters import *


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
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )

    querylist = [
        {'queryset': CategoryType.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': DemobilizedType.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': DrivingLicenseType.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': Organization.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': Borrow.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': Economics.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': Sources.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': EducationType.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': AcademicDegreeType.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': CarType.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': XueLiInformation.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': RenYuanXianZhuang.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': ShenFenGuiLei.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': ChengWei.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': TiJianJieGuo.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': Politics.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': ZhuangTai.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': PermanentType.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': Marriage.objects.filter(is_delete=False), 'serializer_class': TypeSerializer},
        {'queryset': DaduiZhongduiType.objects.filter(is_delete=False), 'serializer_class': DaduiZhongduiTypeSerializer},
        {'queryset': Year.objects.filter(is_delete=False), 'serializer_class': YearSerializer},
    ]


class DaduiZhongduiTypeList(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
     list:大队中队类别
    """
    queryset = DaduiZhongduiType.objects.all()
    serializer_class = DaduiZhongduiTypeSerializer

    filter_backends = [DjangoFilterBackend,  # django_filters过滤
                       ]

    filter_class = DaduiZhongduiTypeFilter


class DiZhiList(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:未标记为删除的人员的籍贯列表
    """
    serializer_class = DiZhiSerializer

    def get_queryset(self):
        return DiZhi.objects.filter(personalinformation__is_delete=False).values('jiguan').distinct().order_by('jiguan')


class DiZhiNotListAll(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:未标记为删除的人员的籍贯列表
    """
    serializer_class = DiZhiSerializer

    def get_queryset(self):
        return DiZhi.objects.filter(personalinformation__is_delete=False).values('jiguan', 'id').distinct().order_by('jiguan')


class CategoryTypeList(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:人员类别
    """

    queryset = CategoryType.objects.all()
    serializer_class = CategoryTypeSerializer

    filter_backends = [DjangoFilterBackend,  # django_filters过滤
                       ]

    filter_class = CategoryTypeFilter
