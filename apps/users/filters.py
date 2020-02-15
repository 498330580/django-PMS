# -*- coding: utf-8 -*-
__author__ = 'bobby'

import django_filters
# from django.db.models import Q
from rest_framework.response import Response

from users.models import PersonalInformation


class PersonalInformationFilter(django_filters.rest_framework.FilterSet):
    """
    人员的过滤类
    """
    # timestart = django_filters.DateTimeFilter(field_name='entry', help_text="开始时间", lookup_expr='gte')
    # timeout = django_filters.DateTimeFilter(field_name='entry', help_text="结束时间", lookup_expr='lte')
    # category = django_filters.CharFilter(field_name='category__name', help_text='人员类别', lookup_expr='icontains')
    # name = django_filters.CharFilter(field_name='name', help_text='名字', lookup_expr='icontains')
    # dadui = django_filters.CharFilter(field_name='dadui', help_text='大队', lookup_expr='icontains')
    # fenzu_dadui = django_filters.CharFilter(field_name='fenzu__name', help_text='大队', lookup_expr='icontains')
    # fenzu_zhongdui = django_filters.CharFilter(field_name='fenzu__name', help_text='中队、小组', lookup_expr='icontains')

    # top_category = django_filters.NumberFilter(method='top_category_filter')
    #
    # def top_category_filter(self, queryset, name, value):
    #     return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
    #         category__parent_category__parent_category_id=value))
    yonggongs__shenfenguileinot__name = django_filters.CharFilter(method='zhuangtainot_filter')
    dangtuannot = django_filters.CharFilter(method='dangtuannot_filter')
    # all = django_filters.CharFilter(method='all_filter')

    def zhuangtainot_filter(self, queryset, name, value):
        if value == '协勤队员':
            return queryset.filter(yonggongs__shenfenguilei__name=value).exclude(yonggongs__zhuangtai__name='转辅')
        else:
            return queryset.filter(yonggongs__shenfenguilei__name=value)

    def dangtuannot_filter(self, queryset, name, value):
        return queryset.filter(dangtuans__politics__name=value, dangtuans__is_effective=True)

    # def all_filter(self, queryset, name, value):
    #     data = queryset.filter(name=value)
    #     usernames = [user for user in data]
    #     return Response(usernames)

    # def zhuangtai_filter(self, queryset, name, value):
    #     if value == '转辅':
    #         return queryset.filter(yonggongs__zhuangtai__name=value)
    #     pass

    class Meta:
        model = PersonalInformation
        # fields = ['name', 'category', 'entry']
        fields = ['dadui', 'fenzu', 'sex', 'dangtuans__politics__name', 'yonggongs__zhuangtai__name', 'jiguan__jiguan',
                  'drivinglicense__name', 'bianzhi__name', 'jiediao__name', 'yonggongs__shenfenguilei__name',
                  'yonggongs__shenfenguileinot__name', 'dangtuannot', 'is_delete']
